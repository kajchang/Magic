import matplotlib.pyplot as plt
import json
import sys


def graph_bar(data):
    degrees = [account["degrees"]
               for account in data if account['toSt4ck']]
    sorted_degrees = [degrees.count(x) for x in range(max(degrees))]

    plt.bar(range(len(sorted_degrees)), sorted_degrees)
    plt.xticks(range(len(sorted_degrees)), range(max(degrees)))
    plt.title("Degrees of Separation from St4ck")
    plt.xlabel("Degrees")
    plt.ylabel("Accounts")
    plt.show()


if __name__ == '__main__':
    if sys.argv[1:]:
        try:
            graph_bar(json.load(open(sys.argv[1])) if sys.argv[1].endswith(
                '.json') else json.load(open('{}.json'.format(sys.argv[1]))))
        except Exception:
            print(
                'Usage:\npython bar.py <filename>')
    else:
        print(
            'Usage:\npython bar.py <filename>')
