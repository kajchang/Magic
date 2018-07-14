import requests
from bs4 import BeautifulSoup
import random
import json
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
    return z * 2 + v + y


def randomFullAccount():
    id_ = steamIdFormula(random.randint(1, 99999999))  # Generate a random id.
    account = BeautifulSoup(requests.get("https://steamcommunity.com/profiles/{}".format(
        id_)).text, "html.parser")

    while not account.find(class_="actual_persona_name") or account.find(class_="profile_private_info") or not account.find(class_="friendBlockLinkOverlay"):
        # Generate a random id.
        id_ = steamIdFormula(random.randint(1, 99999999))
        account = BeautifulSoup(requests.get("https://steamcommunity.com/profiles/{}".format(
            id_)).text, "html.parser")

    return id_


def analyze(id_=randomFullAccount(), data=None):
    """Analyze one steam account.
    Returns:
        Dictionary with:
            path (dict) - path of accounts tested and their levels
            level (int) - level of account analyzed
    """
    id_ = str(id_)  # Convert to string so we can check with .isdigit()

    if id_.isdigit():  # Check if it's a raw id and using according url format
        account = BeautifulSoup(requests.get("https://steamcommunity.com/profiles/{}".format(
            id_)).text, "html.parser")
    else:  # Use url format for aliases
        account = BeautifulSoup(requests.get("https://steamcommunity.com/id/{}".format(
            id_)).text, "html.parser")

    if not data:  # Check if it needs to build on path or start new one.
        data = {account.find(class_="actual_persona_name").text: int(
            account.find(class_="friendPlayerLevelNum").text)}

    if account.find(class_="actual_persona_name").text != "St4ck":  # Check if the account name is St4ck
        if account.find(class_="actual_persona_name").text in list(data.keys())[1:] or not account.find(class_="friendBlockLinkOverlay"):
            # Stop if we"re looping back to previous accounts or if we run into a private account.
            return data

        data[account.find(class_="actual_persona_name").text] = int(
            account.find(class_="friendPlayerLevelNum").text)

        return analyze(account.find(
            class_="friendBlockLinkOverlay")["href"].split('/')[4], data=data)  # Call analyze on the next account

    else:
        data[account.find(class_="actual_persona_name").text] = int(
            account.find(class_="friendPlayerLevelNum").text)

        return data


if __name__ == "__main__":
    if sys.argv[1:]:
        if True:
            filename = sys.argv[2] if sys.argv[2].endswith(
                ".json") else "{}.json".format(sys.argv[2])  # add .json if filename doesn't end with .json
            for x in range(int(sys.argv[1])):
                data = analyze()
                try:
                    file_data = json.load(open(filename)) # Try loading data already in file

                except OSError:
                    with open(filename, "w") as file_:  # Create file if doesn't exist
                        file_data = []
                        file_.write(json.dumps(file_data))

                with open(filename, "w") as file_:
                    file_.write(json.dumps(file_data + [data]))

        else:
            print(
                "Usage:\npython st4ck.py <# of accounts> <filename for data>")
    else:
        print(
            "Usage:\npython st4ck.py <# of accounts> <filename for data>")
