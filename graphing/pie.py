import matplotlib.pyplot as plt
import json

account_data = json.load(open("st4ck.json"))

labels = 'To St4ck', 'Not To St4ck'
sizes = [len([account for account in account_data if account['toSt4ck']]), len([account for account in account_data if not account['toSt4ck']])]
colors = ['lightblue', 'red']

plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()
