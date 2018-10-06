import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import numpy as np


conn = sqlite3.connect("Expenditure.db")
dataframe = pd.read_sql_query("SELECT Item, sum(Cost) as Cost FROM Expenditure group by Item", conn)
conn.close()

print(dataframe)

# dates = dataframe['expenditure_date']
items = dataframe['Item']
costs = dataframe['Cost']

explode = ()
for i in items:
	explode = explode + (0,)

print(explode)

fig1, ax1 = plt.subplots()

ax1.pie(costs, explode = explode, labels = items, autopct='%1.1f%%',
        shadow=True, startangle=90)

ax1.axis('equal')

plt.tight_layout()
plt.show()

n = "05"
conn = sqlite3.connect("Expenditure.db")
dataframe = pd.read_sql_query("SELECT expenditure_date, sum(Cost) as cost FROM Expenditure where expenditure_date like '%-10-%' group by expenditure_date", conn)
conn.close()

print(dataframe)

expenditure_dates = dataframe['expenditure_date']
costs = dataframe['cost']

plt.bar(expenditure_dates, costs)
plt.show()