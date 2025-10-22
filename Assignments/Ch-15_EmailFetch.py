"""
===========================================================
Program Name: Email Fetcher
Author: Robert Hallanger   
Date: 2025-10-15
Description:
    This program performs a fetch of email addresses from Google Sheets API.
    It is designed to grab emails.
    
Usage:
    Run the script using Python 3.14. Ensure all dependencies
    are installed before execution.

===========================================================
"""
import ezsheets
import time

### To use ezsheets for Google Sheets, you will need to use Google's Cloud Console
# Enable Drive API and Sheets API
# Create an OAuth Consent and generate credentials for this python desktop app.
# Rename and transfer the downloaded JSON credentials from client_secret_*.json to credentials-sheets.json
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Do not share these credentials !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

emails = []  # Initialize emails list globally
### This function will be used after the initial fetch and print of emails to gather any new emails added to the sheet.
def emailRefresh():
    # Imports the empty email list to prevent repetition of already found emails.
    global emails
    # fetches the overall google sheets workbook
    workbook = ezsheets.Spreadsheet('https://docs.google.com/spreadsheets/d/1vWAR-nN2S99h3_Af6voad7Ux1ynCXmHbmLiAEd_CWsU/edit?resourcekey=&gid=590686694#gid=590686694') #reinitializes every loop to gather new emails.
    # Google Sheets is confusing with sheet of sheets.
    # Sheet refers to the page we have selected at the bottom of the page.
    # Workbook refers to the entire document with multiple sheets.
    # ResponseSheet is grabs the whole sheet from the workbook's list of sheets.
    responseSheet = workbook[0]
    # Grabs column B which contains the emails.
    newEmails = responseSheet.getColumn('B')
    # Filters out any empty cells and the header 'Email Address'
    newEmails = list(filter(None, newEmails))
    newEmails.remove('Email Address')
    # Compares new emails to existing emails and appends any new ones to the emails list.
    # While printing any new emails found.
    currentTime = time.strftime("%H:%M:%S")
    for i in newEmails:
        if i not in emails:
            emails.append(i)
            print(f'[{currentTime}] {i}')
    time.sleep(30) # Delay before next refresh to reduce API calls.

currentTime = time.strftime("%a, %d %b %Y %H:%M:%S") #timestamps
print(f'[{currentTime}] Emails found in responses:')
# Infiinite loop to keep refreshing emails
while True:
    emailRefresh()