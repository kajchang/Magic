import matplotlib.pyplot as plt
import json
import sys


def graph_line(data):
    for a in data:
        plt.plot(range(len(a["path"])), list(a["path"].values()))

    plt.xlabel('Degrees')
    plt.ylabel('Level')
    plt.title('Level over Degrees from St4ck')

    plt.show()


if __name__ == '__main__':
    if sys.argv[1:]:
        try:
            graph_line(json.load(open(sys.argv[1])) if sys.argv[1].endswith(
                '.json') else json.load(open('{}.json'.format(sys.argv[1])))).show()
        except Exception:
            print(
                'Usage:\npython line.py <filename>')
    else:
        print(
            'Usage:\npython line.py <filename>')
