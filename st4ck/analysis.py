import requests
from bs4 import BeautifulSoup

import random
import sys


def steamIdFormula(z, v=0x0110000100000000, y=1):
    """Formula for converting Steam ID to Steam Community ID
    From https://developer.valvesoftware.com/wiki/SteamID
    Args:
        v (int, optional) : account type, defaults to user: 0x0110000100000000
        y (int, optional) : account universe, defaults to public: 1
        z (int) : account id
    Returns:
        Steam Community ID (int)
    """
    return 2 * z + v + y


def isValidId(id_, v=0x0110000100000000, y=1):
    """Reverse Steam ID formula taking full community ID and decoding the account ID.
    Args:
        id_ (int) : steam community id
        v (int, optional) : account type, defaults to user: 0x0110000100000000
        y (int, optional) : account universe, defaults to public: 1

    Returns:
        True: ID is valid.
        False: ID is invalid.
    """
    z = (id_ - y - v) / 2
    
    return z >= 1 and z <= 999999999


def randomFullAccount():
    """Generate a random account that exists and is not private.
    Returns:
        Valid Steam Community ID (int)
    """
    id_ = steamIdFormula(random.randint(1, 999999999))  # Generate a random id.
    account = BeautifulSoup(requests.get("https://steamcommunity.com/profiles/{}".format(
        id_)).text, "html.parser")

    while not account.find(class_="actual_persona_name") or account.find(class_="profile_private_info") or not account.find(class_="friendBlockLinkOverlay"):
        # Generate a random id.
        id_ = steamIdFormula(random.randint(1, 99999999))
        account = BeautifulSoup(requests.get("https://steamcommunity.com/profiles/{}".format(
            id_)).text, "html.parser")

    return id_


def analyze(id_=randomFullAccount, data=None, verbose=False):
    """Analyze one steam account.
    Returns:
        Dictionary mapping account names to their levels.
    """
    if callable(id_): # Call ID generator function if function is passed as id_ param.
        id_ = id_()

    id_ = str(id_)  # Convert to string so we can check with .isdigit()

    if id_.isdigit() and isValidId(int(id_)):  # Check if it's a raw id and using according url format
        account = BeautifulSoup(requests.get("https://steamcommunity.com/profiles/{}".format(
            id_)).text, "html.parser")

    else:  # Use url format for aliases
        account = BeautifulSoup(requests.get("https://steamcommunity.com/id/{}".format(
            id_)).text, "html.parser")

    name = account.find(class_="actual_persona_name").text

    if not data:  # Check if it needs to build on path or start new one.
        if verbose:
            print('Scraping {}'.format(name.translate(dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd))))

        data = {name: int(
            account.find(class_="friendPlayerLevelNum").text)}

        return analyze(account.find(
            class_="friendBlockLinkOverlay")["href"].split('/')[4], data=data, verbose=verbose)  # Call analyze on the next account

    if name != "St4ck":  # Check if the account name is St4ck
        if name in data or not account.find(class_="friendBlockLinkOverlay"):
            # Stop if we"re looping back to previous accounts or if we run into a private account.
            if verbose:
                print('Finished at {}'.format(name))

            return data

        data[name] = int(
            account.find(class_="friendPlayerLevelNum").text)

        if verbose:
            print('Scraping {}'.format(name.translate(dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd))))

        return analyze(account.find(
            class_="friendBlockLinkOverlay")["href"].split('/')[4], data=data, verbose=verbose)  # Call analyze on the next account

    else:
        if verbose:
            print('Finished at St4ck')

        data[name] = int(
            account.find(class_="friendPlayerLevelNum").text)

        return data
