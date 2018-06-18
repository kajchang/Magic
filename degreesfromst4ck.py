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


def analyzeOne():
    """Analyze one steam account.
    Returns:
        Dictionary with:
        toSt4ck (bool) - whether the account led to St4ck or not
        degrees (int) - number of accounts tested
        path - path of accounts tested
        level - level of account analyzed
    """
    # Record accounts that deadend (don't lead to St4ck)
    while True:
        account = BeautifulSoup(requests.get("https://steamcommunity.com/profiles/{}".format(
            steamIdFormula(random.randint(1, 99999999)))).text, "html.parser")

        if not account.find(class_="actual_persona_name") or account.find(class_="profile_private_info") or not account.find(class_="friendBlockLinkOverlay"):
            # Skip the user if unregistered or account is private or has no friends
            continue

        path = {}
        level = int(account.find(class_="friendPlayerLevelNum").text)

        while account.find(class_="actual_persona_name").text != "St4ck":

            account = BeautifulSoup(requests.get(account.find(
                class_="friendBlockLinkOverlay")["href"]).text, "html.parser")

            if account.find(class_="actual_persona_name").text in path or not account.find(class_="friendBlockLinkOverlay"):
                # Stop if we"re looping back to previous accounts or if we run into a private account
                return {"toSt4ck": False,
                        "degrees": len(path),
                        "path": path,
                        "level": level}

            path[account.find(class_="actual_persona_name").text] = int(
                account.find(class_="friendPlayerLevelNum").text)

        return {"toSt4ck": True,
                "degrees": len(path),
                "path": path,
                "level": level}
