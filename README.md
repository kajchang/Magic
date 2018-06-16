# st4ck analysis

```degreesfromst4ck.py``` is a basic scraper that gets a random Steam account and then follows the highest-level friend until it reaches the highest level Steam user, St4ck, or runs into a private account or an account it's seen before. 

To use it, install the requirements with ```pip install -r requirements.txt```.

The script has a basic scraping function that can be run however you want, whether that be in a loop, or with multiprocessing/ threading.

After getting some results, write them to a ```.json``` file, then move it to the graphing folder, install the graphing requirements, and run any of the graphing examples: ```pie.py```, ```bar.py```, and ```sankey.py```. 

The pie and bar charts use matplotlib, and the sankey chart uses [plot.ly](https://plot.ly/), so you need to set up your API key before generating the sankey chart.

```bar.py```:
![bar.png](https://github.com/kajchang/degrees-from-st4ck/raw/master/graphing/bar.png)

Graphs the distribution of accounts' degrees of separation from St4ck.

```pie.py```:
![pie.png](https://github.com/kajchang/degrees-from-st4ck/raw/master/graphing/pie.png)

Shows the percentage of accounts that led to St4ck and the percentage that didn't.

```sankey.py```:
![sankey.png](https://github.com/kajchang/degrees-from-st4ck/raw/master/graphing/sankey.png)

Shows the flow of users to St4ck, it's hard to see in a single image because of the volume of links and nodes. See and explore it on plot.ly [here](https://plot.ly/~kachang/16/the-path-to-st4ck/#/).

I hope this entertained you!
