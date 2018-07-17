import requests
from bs4 import BeautifulSoup

import random

import plotly.plotly as py


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


def analyze(id_=randomFullAccount, data=None, verbose=False):
    """Analyze one steam account.
    Returns:
        Dictionary with:
            path (dict) - path of accounts tested and their levels
            level (int) - level of account analyzed
    """
    if callable(id_):
        id_ = id_()

    id_ = str(id_)  # Convert to string so we can check with .isdigit()

    if id_.isdigit():  # Check if it's a raw id and using according url format
        account = BeautifulSoup(requests.get("https://steamcommunity.com/profiles/{}".format(
            id_)).text, "html.parser")
    else:  # Use url format for aliases
        account = BeautifulSoup(requests.get("https://steamcommunity.com/id/{}".format(
            id_)).text, "html.parser")

    name = account.find(class_="actual_persona_name").text

    if not data:  # Check if it needs to build on path or start new one.
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
            print('Scraping {}'.format(name))

        return analyze(account.find(
            class_="friendBlockLinkOverlay")["href"].split('/')[4], data=data, verbose=verbose)  # Call analyze on the next account

    else:
        if verbose:
            print('Finished at St4ck')

        data[name] = int(
            account.find(class_="friendPlayerLevelNum").text)

        return data


def graph_line(data):
    for a in data:
        plt.plot(range(len(a)), list(a.values()))

    plt.xlabel('Degrees')
    plt.ylabel('Level')
    plt.title('Level over Degrees from St4ck')

    plt.show()


def graph_pie(data):
    labels = 'To St4ck', 'Not To St4ck'
    sizes = [len([account for account in data if list(account.keys())[-1] == 'St4ck']),
             len([account for account in data if not list(account.keys())[-1] == 'St4ck'])]
    colors = ['lightblue', 'red']

    plt.pie(sizes, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()


def graph_bar(data):
    degrees = [len(account)
               for account in data if list(account.keys())[-1] == 'St4ck']

    sorted_degrees = [degrees.count(x) for x in range(max(degrees) + 1)]

    plt.bar(range(len(sorted_degrees)), sorted_degrees)
    plt.xticks(range(len(sorted_degrees)), range(max(degrees) + 1))
    plt.title("Degrees of Separation from St4ck")
    plt.xlabel("Degrees")
    plt.ylabel("Accounts")
    plt.show()


def graph_sankey(data):
    labels = list(
        set([a for p in data for a in list(p.keys())]))

    links = {}

    for p in data:
        for a in list(p.keys())[:-1]:
            if (a, list(p.keys())[list(p.keys()).index(a) + 1]) in links:
                links[(a, list(p.keys())[
                       list(p.keys()).index(a) + 1])] += 1
            else:
                links[(a, list(p.keys())[
                       list(p.keys()).index(a) + 1])] = 1

    indexed_links = [
        [labels.index(x[0]), labels.index(x[1]), links[x]] for x in links]

    source = [x[0] for x in indexed_links]
    target = [x[1] for x in indexed_links]
    value = [x[2] for x in indexed_links]

    data = dict(
        type="sankey",
        node=dict(
            pad=15,
            thickness=20,
            line=dict(
                color="black",
                width=0.5
            ),
            label=labels,
            color=["blue" for x in range(len(labels))]
        ),
        link=dict(
            source=source,
            target=target,
            value=value
        )
    )

    layout = dict(
        title="The Path to St4ck",
        font=dict(
            size=10
        )
    )

    fig = dict(data=[data], layout=layout)
    py.iplot(fig, validate=False)

if __name__ == '__main__':
    import matplotlib.pyplot as plt
