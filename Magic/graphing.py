import plotly.plotly as py


def graph_line(data):
    import matplotlib.pyplot as plt
    for a in data:
        plt.plot(range(len(a)), list(a.values()))

    plt.xlabel('Degrees')
    plt.ylabel('Level')
    plt.title('Level over Degrees from Magic')

    plt.show()


def graph_pie(data):
    import matplotlib.pyplot as plt
    labels = 'To Magic', 'Not To Magic'
    sizes = [len([account for account in data if list(account.keys())[-1] == 'Magic']),
             len([account for account in data if not list(account.keys())[-1] == 'Magic'])]
    colors = ['lightblue', 'red']

    plt.pie(sizes, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.show()


def graph_bar(data):
    import matplotlib.pyplot as plt
    degrees = [len(account)
               for account in data if list(account.keys())[-1] == 'Magic']

    sorted_degrees = [degrees.count(x) for x in range(max(degrees) + 1)]

    plt.bar(range(len(sorted_degrees)), sorted_degrees)
    plt.xticks(range(len(sorted_degrees)), range(max(degrees) + 1))
    plt.title('Degrees of Separation from Magic')
    plt.xlabel('Degrees')
    plt.ylabel('Accounts')
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
        type='sankey',
        node=dict(
            pad=15,
            thickness=20,
            line=dict(
                color='black',
                width=0.5
            ),
            label=labels,
            color=['blue' for x in range(len(labels))]
        ),
        link=dict(
            source=source,
            target=target,
            value=value
        )
    )

    layout = dict(
        title='The Path to Magic',
        font=dict(
            size=10
        )
    )

    fig = dict(data=[data], layout=layout)
    py.iplot(fig, validate=False)
