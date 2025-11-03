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
dayWeekVar = time.strftime("%A")
todayVar = datetime.datetime.now()
scanDelta = datetime.timedelta(days=1) #Adjustable to scan negative time or positive time.
option = ''

######### FUNCTIONS #########
def nextFridayScan(todayVar, userCount):
	fridayCounter = 0
	# Loops until the user specified number of Friday the 13ths are found
	while fridayCounter < userCount:
		if todayVar.day == 13 and dayWeekVar == "Friday":
			print("Found Friday the 13th on: ", todayVar)
			fridayCounter += 1
		todayVar += scanDelta
		dayWeekVar = todayVar.strftime("%A")

while option not in ['next', 'previous']:
	option = input("Type 'next' to find the next 10 Friday the 13ths or 'previous' to find the previous 10 Friday the 13ths: ").strip().lower()
	if option == 'previous':
		scanDelta = datetime.timedelta(days=-1)
	elif option == 'next':
		scanDelta = datetime.timedelta(days=1)
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
		print('Value entere is 0 or less. Please try again.')

nextFridayScan(todayVar, userCount)
input('Press enter to continue...')