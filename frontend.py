# Expenditure Management
from database import main_function
import getpass # for password input
from datetime import date # get todays date
from report import generator

def display_head():
	print()
	print("--------------------------------------------------------------------------------")
	print("-----------------Welcome to the Expenditure Management System-------------------")
	print("--------------------------------------------------------------------------------")
	print()

def prompt_frontend():
	print()
	print("1) Credentials ")
	print("2) Enter Expenditure")
	print("3) Generate Report")
	print("4) Exit")
	print()
	n = int(input("Enter your choice: "))
	return n

def credentials():
	email = input("Enter your E-mail ID: ")
	password = getpass.getpass()
	return email, password
	

display_head()

flag = 1


while flag == 1:

	choice = prompt_frontend()
	

	if choice == 1:
		email_id, password = credentials()

	elif choice == 2:
		main_function()
		q = input("Do you have more items to enter: ")
		if q == 'y' or q == 'Y':
			flag = 1
		else:
			flag = 0

	elif choice == 3:
		month = int(input('Enter the month number: '))
		generator(month)
		flag = 0
	else:
		flag = 0

	if flag == 0:
		print('\nThank You\n')




