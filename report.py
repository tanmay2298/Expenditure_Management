import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import numpy as np


conn = sqlite3.connect("Expenditure.db")
dataframe = pd.read_sql_query("SELECT * FROM Expenditure", conn)
conn.close()

print(dataframe)

dates = dataframe['Expenditure_Date']
items = dataframe['Item']
costs = dataframe['Cost']

# dates_cost = []
# for i in dates:
# 	temp = i
# 	for j in dates:
# 		if j == i:
# 			dates_cost.append()
explode = ()
for i in dates:
	explode = explode + (0,)

print(explode)

fig1, ax1 = plt.subplots()

ax1.pie(costs, explode = explode, labels = items, autopct='%1.1f%%',
        shadow=True, startangle=90)

ax1.axis('equal')

plt.tight_layout()
plt.show()