import sqlite3
from datetime import date # get todays date

def create_table():
	conn = sqlite3.connect("Expenditure.db")
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS Expenditure(ID INTEGER PRIMARY KEY, expenditure_date text, Item text, Cost real)")
	conn.commit()
	conn.close()

def insert_data(expenditure_date, item, cost):
	conn = sqlite3.connect("Expenditure.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO Expenditure VALUES (NULL, ?, ?, ?)", (expenditure_date, item, cost))
	conn.commit()
	conn.close()

def display_data():
	conn = sqlite3.connect("Expenditure.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM Expenditure")
	data = cur.fetchall()
	conn.close()
	for i in data:
		print(i)

def prompt_database():

	while True:
		print()
		print("1) Make an entry for today")
		print("2) Any other date")
		print()

		n = int(input("Enter your choice: "))
		
		if n == 1:
			Expenditure_Date = str(date.today())
			print(Expenditure_Date)
			break
		elif n == 2:
			Expenditure_Date = input("Enter the date: ")
			break
		else:
			print("Invalid Choice\n", "Retry")

	return Expenditure_Date


def main_function():
	create_table()
	Expenditure_Date = prompt_database()

	item = input("Expenditure on which Item: ")
	cost = float(input("Cost of the Item: "))

	print("Expenditure_Date: ", Expenditure_Date)
	print("Item: ", item)
	print("Cost: ", cost)

	insert_data(Expenditure_Date, item, cost)
	print()
	print("CAUTION: PLEASE MAKE SURE THAT YOUR DATABASE IS NOT OPEN \nELSEWHERE IN SOME DB VIEWING APPLICATION")
	print("....... Data Successfully Entered in Database ........")
	print()
	ch = input("Do you want to see the data: ")
	if (ch == 'Y') or (ch == 'y'):
		display_data()

