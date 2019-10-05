# Expenditure Management
from database import main_function
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
	print("1) Enter Expenditure")
	print("2) Generate Report")
	print("3) Exit")
	print()
	n = int(input("Enter your choice: "))
	return n	

display_head()

flag = 1

while flag == 1:

	choice = prompt_frontend()
	

	if choice == 1 : 
		main_function()
		q = input("Do you have more items to enter: ")
		if q == 'y' or q == 'Y':
			flag = 1
		else:
			flag = 0

	elif choice == 2 :
		month = int(input('Enter the month number: '))
		send_email = input('Want detailed report emailed y/n ?')
		if send_email == 'y' : 
			generator(month , True )
		else : 
			generator(month , False )
			

		flag = 0
	elif choice == 3 :
		flag = 0

	if flag == 0:
		print('\nThank You\n')



