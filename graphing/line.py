import matplotlib.pyplot as plt
import json

account_data = json.load(open("st4ck.json"))

for a in account_data:
    plt.plot(range(len(a["path"])), list(a["path"].values()))

plt.xlabel('Degrees')
plt.ylabel('Level')
plt.title('Level over Degrees from St4ck')

plt.show()
