# Expenditure Management
from database import main_function
import getpass # for password input
from datetime import date # get todays date
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
	flag = 0

	if choice == 1:
		email_id, password = credentials()

	elif choice == 2:
		main_function()

	elif choice == 3:
		month = int(input('Enter the month number: '))

	else:
		print('Wrong Input....Program will be restarted: ')
		flag = 1


