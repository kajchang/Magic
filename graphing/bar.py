import matplotlib.pyplot as plt
import json

account_data = json.load(open("st4ck.json"))

degrees = [account["degrees"] for account in account_data if account['toSt4ck']]
sorted_degrees = [degrees.count(x) for x in range(max(degrees))]

plt.bar(range(len(sorted_degrees)), sorted_degrees)
plt.xticks(range(len(sorted_degrees)), range(max(degrees)))
plt.title("Degrees of Separation from St4ck")
plt.xlabel("Degrees")
plt.ylabel("Accounts")
plt.show()
