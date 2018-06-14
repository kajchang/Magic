import requests
from bs4 import BeautifulSoup
import random


def steam_id_formula(z, v=0x0110000100000000, y=1):
    """Formula for converting Steam ID to Steam Community ID
    From https://developer.valvesoftware.com/wiki/SteamID
    Args:
        v (int, optional) : account type, defaults to user: 0x0110000100000000
        y (int, optional) : account universe, defaults to public: 1
        z (int) : account id
    """
    return z * 2 + v + y


def analyzeSteamAccounts(count=100):
    """Checks specified amount of steam accounts for degrees from St4ck
    Args:
        count (int, optional) : number of steam accounts to check, defaults to 100
    """

    # Using variable instead of range because of unregistered/ private account ids
    accounts_checked = 0
    account_data = []

    while accounts_checked < count:
        accounts_to_st4ck = 0

        account = BeautifulSoup(requests.get(
            'https://steamcommunity.com/profiles/{}'.format(steam_id_formula(random.randint(1, 99999999)))).text, 'html5lib')

        if not account.find('span', {'class': 'actual_persona_name'}) or account.find('div', {'class': 'profile_private_info'}) or not account.find_all('a', {'class': 'friendBlockLinkOverlay'}):
            # Skip the user if unregistered or account is private 0r has no friends :(
            continue

        while account.find('span', {'class': 'actual_persona_name'}).text != 'St4ck':
            account = BeautifulSoup(requests.get(account.find(
                'a', {'class': 'friendBlockLinkOverlay'})['href']).text, 'html5lib')
            accounts_to_st4ck += 1

        account_data.append(accounts_to_st4ck)
        accounts_checked += 1

    return account_data
