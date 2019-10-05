import matplotlib.pyplot as plt
import pandas as pd
import sqlite3
import numpy as np
import send_email as SM

def generator(m , send_email):
	str_condition = "'%-" + str(m) + "-%'"

	query1 = "SELECT Item, sum(Cost) as Cost FROM Expenditure where expenditure_date like " + str_condition + " group by Item order by Cost"
	query2 = "SELECT expenditure_date, sum(Cost) as cost FROM Expenditure where expenditure_date like " + str_condition + " group by expenditure_date"
	query3 = "SELECT sum(Cost) as total_cost FROM Expenditure where expenditure_date like " + str_condition


	conn = sqlite3.connect("Expenditure.db")
	dataframe = pd.read_sql_query(query1, conn)
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
	plt.savefig('pie_chart.png')
	plt.show()


	plt.bar(items, costs)
	plt.savefig('bar_chart1.png')
	plt.show()


	conn = sqlite3.connect("Expenditure.db")
	dataframe = pd.read_sql_query(query2, conn)
	conn.close()

	print(dataframe)

	expenditure_dates = dataframe['expenditure_date']
	costs = dataframe['cost']

	plt.bar(expenditure_dates, costs)
	plt.savefig('bar_chart2.png')
	plt.show()


	conn = sqlite3.connect("Expenditure.db")
	dataframe = pd.read_sql_query(query3, conn)
	conn.close()

	if send_email == True : 
		SM.send_report ( ['bar_chart1.png' , 'bar_chart2.png' , 'pie_chart.png'] , m ) 

	print(dataframe)