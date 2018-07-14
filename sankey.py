import plotly.plotly as py
import json
import sys


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


if __name__ == '__main___':
    if sys.argv[1:]:
        try:
            graph_sankey(json.load(open(sys.argv[1])) if sys.argv[1].endswith(
                '.json') else json.load(open('{}.json'.format(sys.argv[1]))))
        except Exception:
            print(
                'Usage:\npython sankey.py <filename>')
    else:
        print(
            'Usage:\npython sankey.py <filename>')
