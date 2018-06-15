import plotly.plotly as py
import json

account_data = json.load(open("st4ck.json"))

labels = list(set([a for p in account_data for a in p["path"]]))

links = {}

for p in account_data:
    for a in p["path"][:-1]:
        if (a, p["path"][p["path"].index(a) + 1]) in links:
            links[(a, p["path"][p["path"].index(a) + 1])] += 1
        else:
            links[(a, p["path"][p["path"].index(a) + 1])] = 1

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
