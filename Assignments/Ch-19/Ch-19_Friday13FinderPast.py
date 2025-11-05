"""
===========================================================
Program Name: Firday the 13th Finder Past
Author: Robert Hallanger
Date: 2025-11-3
Description:
This program performs a quick search for the prior 10 Friday the 13ths.

Usage:
Run the script using Python 3.13. Ensure all dependencies
are installed before execution.
===========================================================
"""
import datetime
import time

todayVar = datetime.datetime.now()
scanDeltaDays = datetime.timedelta(days=-1)

def nextFridayScan(todayVar):
	fridayCounter = 0
	todayPrint = todayVar.strftime("%B %Y")
	while todayVar.year >= 1:
		if todayVar.day == 13 and dayWeekVar == "Friday":
			if fridayCounter < 10:
				print("Found Friday the 13th in: ", todayPrint)
			elif fridayCounter == 10:
				print("""
-------------------------------------------------
Closest 10 Friday the 13ths have been detailed
-------------------------------------------------

-------------------------------------------------
Finding months with Friday the 13th until year 1
-------------------------------------------------
				""")
				print("Friday the 13th found in: ", todayPrint)
			else:
				print("Friday the 13th found in: ", todayPrint)
			fridayCounter += 1
		try:
			todayVar += scanDeltaDays
			todayYear = todayVar.strftime("%Y")
			todayMonth = todayVar.strftime("%B")
			todayPrint = todayMonth + " " + todayYear.lstrip('0')
			dayWeekVar = todayVar.strftime("%A")
		except:
			break


nextFridayScan(todayVar)
input('Press any key to continue . . .')