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

dayWeekVar = time.strftime("%A")
todayVar = datetime.datetime.now()
scanDelta = datetime.timedelta(days=1)

print(todayVar)

def nextFridayScan(todayVar):
	fridayCounter = 0
	while fridayCounter < 10:
		if todayVar.day == 13 and dayWeekVar == "Friday":
			print("Found Friday the 13th on: ", todayVar)
			fridayCounter += 1
		todayVar += scanDelta
		dayWeekVar = todayVar.strftime("%A")

nextFridayScan(todayVar)
input('Press enter to continue...')