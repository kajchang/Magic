# st4ck analysis

Have you ever noticed that if you continuously follow your highest-level steam friend and then their highest-level steam friend and so on, most of the time, you'll find St4ck, the highest level Steam account, at the top of the pile?

```st4ck.py``` gets a random Steam account and follows this method to see if it'll reach St4ck or not.


## How to Use

First, install the required packages with ```pip install -r requirements.txt```.

Next, get some results with ```python3 st4ck.py <# of accounts> <filename for data>```

After getting some results, run any of the graphing examples: ```pie.py```, ```line.py```, ```bar.py```, and ```sankey.py``` like this: ```python3 line.py <filename with the data>```

The pie, bar, and line charts use matplotlib, but the sankey chart uses [plot.ly](https://plot.ly/) so you'll need to set up your API key before generating the sankey chart.

```bar.py```:
![bar.png](https://github.com/kajchang/degrees-from-st4ck/raw/master/graphing/bar.png)

Graphs the distribution of accounts' degrees of separation from St4ck.

```pie.py```:
![pie.png](https://github.com/kajchang/degrees-from-st4ck/raw/master/graphing/pie.png)

Shows the percentage of accounts that led to St4ck and the percentage that didn't.

```sankey.py```:
![sankey.png](https://github.com/kajchang/degrees-from-st4ck/raw/master/graphing/sankey.png)

Shows the flow of users to St4ck, it's hard to see in a single image because of the volume of links and nodes. See and explore it on plot.ly [here](https://plot.ly/~kachang/16/the-path-to-st4ck/#/).

```line.png```:
![line.png](https://github.com/kajchang/degrees-from-st4ck/raw/master/graphing/line.png)

Shows how the level rises as the accounts get closer to St4ck.
