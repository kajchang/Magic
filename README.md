# Doesn't work anymore with the new version of Steam because profile's friends are hidden by default.


# st4ck analysis

Have you ever noticed that if you continuously follow your highest-level steam friend and then their highest-level steam friend and so on, most of the time, you'll find St4ck, the highest level Steam account, at the top of the pile?

```st4ck.py``` gets a random Steam account and follows this method to see if it'll reach St4ck or not.


## How to Use

First, clone or download this repository.

Next, install the required packages with `$ pip install -r requirements.txt`.

To generate some results from random account:

```bash
$ python3 run.py -f data.json -n 5 -v
```

This will generate 5 results, dump the results into ```data.json```, and turn on verbosity. To run without verbosity, just leave out the ```-v```.

To get results from a preset account:

```bash
$ python3 run.py -f data.json -id 76561198045813683
```

or 

```bash
$ python3 run.py -f data.json -id kachangred
```

To graph:

```bash
$ python3 run.py -pie -f data.json
```

This will read data from data.json and generate a pie chart from it. Other valid graphing options are ```-bar```, ```-line```, and ```-sankey```.

The pie, bar, and line charts use matplotlib, but the sankey chart uses [plot.ly](https://plot.ly/) so you'll need to set up your API key before generating the sankey chart.

```bar.py```:
![bar.png](https://github.com/kajchang/st4ck/raw/master/images/bar.png)

Graphs the distribution of accounts' degrees of separation from St4ck.

```pie.py```:
![pie.png](https://github.com/kajchang/st4ck/raw/master/images/pie.png)

Shows the percentage of accounts that led to St4ck and the percentage that didn't.

```sankey.py```:
![sankey.png](https://github.com/kajchang/st4ck/raw/master/images/sankey.png)

Shows the flow of users to St4ck, it's hard to see in a single image because of the volume of links and nodes. See and explore it on plot.ly [here](https://plot.ly/~kachang/16/the-path-to-st4ck/#/).

```line.png```:
![line.png](https://github.com/kajchang/st4ck/raw/master/images/line.png)

Shows how the level rises as the accounts get closer to St4ck.
