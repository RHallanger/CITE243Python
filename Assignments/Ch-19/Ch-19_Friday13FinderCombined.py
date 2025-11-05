"""
===========================================================
Program Name: Firday the 13th Finder Future
Author: Robert Hallanger
Date: 2025-11-3
Description:
This program performs a quick search for the next 10 Friday the 13th.

Usage:
Run the script using Python 3.13. Ensure all dependencies
are installed before execution.
===========================================================
"""
import datetime
import time

######### VARIABLES #########
todayVar = datetime.datetime.now() # Grabs today as starting point.
option = ''

######### FUNCTIONS #########
def nextFridayScan(todayVar, userCount):
	fridayCounter = 0
	dayWeekVar = todayVar.strftime("%A") # initial day of the week variable
	# Loops until the user specified number of encounters
	while fridayCounter < userCount:
		# Checks if both friday and the 13th align and prints it if so.
		if todayVar.day == 13 and dayWeekVar == "Friday":
			print("Found Friday the 13th on: ", todayVar)
			fridayCounter += 1
		# Advances the day by one
		todayVar += scanDelta
		dayWeekVar = todayVar.strftime("%A") #refreshes the fomral day of the week variable

while option not in ['next', 'previous']:
	option = input("Use the keywords 'next' or 'previous' to find relevant Friday the 13th occurences: ").strip().lower()
	if option == 'previous':
		scanDelta = datetime.timedelta(days=-1) # Increments the date backwards by one day
	elif option == 'next':
		scanDelta = datetime.timedelta(days=1) # Increments the date forwards by one day
	else:
		print("Invalid option. Please type 'next' or 'previous'.")

while True:
	try:
		userCount = int(input('How many Friday the 13ths would you like to see?: '))

	except:
		print('Value entered is not a valid whole number. Please try again.')

	if userCount > 0:
		break
	else:
		print('Value entered is 0 or less. Please try again.')

nextFridayScan(todayVar, userCount)
input('Press any key to continue . . .')