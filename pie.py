import matplotlib.pyplot as plt
import json
import sys


def graph_pie(data):
    labels = 'To St4ck', 'Not To St4ck'
    sizes = [len([account for account in data if list(account.keys())[-1] == 'St4ck']),
             len([account for account in data if not list(account.keys())[-1] == 'St4ck'])]
    colors = ['lightblue', 'red']

    plt.pie(sizes, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()


if __name__ == '__main__':
    if sys.argv[1:]:
        try:
            graph_pie(json.load(open(sys.argv[1])) if sys.argv[1].endswith(
                '.json') else json.load(open('{}.json'.format(sys.argv[1]))))
        except Exception as e:
            if not isinstance(e, AttributeError):
                print(
                    'Usage:\npython pie.py <filename>')
    else:
        print(
            'Usage:\npython pie.py <filename>')
