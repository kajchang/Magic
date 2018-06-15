# st4ck analysis

```degreesfromst4ck.py``` is a basic scraper script that gets random Steam accounts and then gets on the highest-level friend until it reaches St4ck, the highest level Steam user. The script isn't that well structured because I was using it personally. 

To use it, install the requirements with ```pip install -r requirements.txt```.

Basically, use the ```analyzeOne()``` function, either in a loop or with multiprocessing (```analyzeSteamAccounts```), and write the results to a ```.json``` file, then move it to the graphing folder, install the requirements, and run any of the graphing examples: ```pie.py```, ```bar.py```, and ```sankey.py```. The pie and bar charts use matplotlib, but the sankey chart uses [plot.ly](https://plot.ly/), so you need to set up your API key before generating the sankey chart.

```bar.py```:
![bar.png](https://github.com/kajchang/degrees-from-st4ck/raw/master/graphing/bar.png)

Graphs the distribution of accounts' degrees of separation from St4ck.

```pie.py```:
![pie.png](https://github.com/kajchang/degrees-from-st4ck/raw/master/graphing/pie.png)

Shows the percentage of accounts that led to St4ck and the percentage that didn't.

```sankey.py```:
![sankey.png](https://github.com/kajchang/degrees-from-st4ck/raw/master/graphing/sankey.png)

Shows the flow of users to St4ck, it's hard to see in an image because of the volume of links and nodes. See and explore it on plot.ly [here](https://plot.ly/~kachang/16/the-path-to-st4ck/#/).

I hope this entertained you.
