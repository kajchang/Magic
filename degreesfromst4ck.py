from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup
import random


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
    return z * 2 + v + y


def analyzeOne(_=None):
    """Analyze one steam account.
    Args:
        _ : placeholder for p.map argument.
    Returns:
        Dictionary with:
        deadends - number of accounts found that don't lead St4ck.
        degrees - number of accounts to St4ck.
        path - path of accounts to St4ck.
        level - level of account analyzed.
    """
    # Record accounts that deadend (don't lead to St4ck)
    deadends = 0

    while True:
        account = BeautifulSoup(requests.get("https://steamcommunity.com/profiles/{}".format(
            steamIdFormula(random.randint(1, 99999999)))).text, "html5lib")

        if not account.find(class_="actual_persona_name") or account.find(class_="profile_private_info") or not account.find(class_="friendBlockLinkOverlay"):
            # Skip the user if unregistered or account is private or has no friends
            continue

        path = []
        level = int(account.find(class_="friendPlayerLevelNum").text)

        while account.find(class_="actual_persona_name").text != "St4ck":

            if not account.find(class_="friendBlockLinkOverlay"):
                # Stop if we run into a private account
                path = None
                break

            account = BeautifulSoup(requests.get(account.find(
                class_="friendBlockLinkOverlay")["href"]).text, "html5lib")

            if account.find(class_="actual_persona_name").text in path:
                # Stop if we"re looping back to previous accounts
                deadends += 1
                path = None
                break

            path.append(account.find(class_="actual_persona_name").text)

        if path:
            return {"deadends": deadends,
                    "degrees": len(path),
                    "path": path,
                    "level": level}


def analyzeSteamAccounts(processes, count=100):
    return Pool(processes).map(analyzeOne, range(count))
