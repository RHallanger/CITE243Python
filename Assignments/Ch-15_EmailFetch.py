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

### To use ezsheets for Google Sheets, you will need to use Google's Cloud Console
# Enable Drive API and Sheets API
# Create an OAuth Consent and generate credentials for this python desktop app.
# Rename and transfer the downloaded JSON credentials from client_secret_*.json to credentials-sheets.json
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Do not share these credentials !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

### assign the Google Sheets workbook we want to workbook
workbook = ezsheets.Spreadsheet('https://docs.google.com/spreadsheets/d/1vWAR-nN2S99h3_Af6voad7Ux1ynCXmHbmLiAEd_CWsU/edit?resourcekey=&gid=590686694#gid=590686694')

### This specifies the sheet in the workbook we actually want to look at.
# Sheets are the little tabs at the bottom of the page that leads to a different table.
responseSheet = workbook[0]
### Now we copy everything in the column that we want to a list labeled emails.
emails = responseSheet.getColumn('B')
### Now we have a lot of None data types that make up roughly 100 list items.
# So we are going to filter all None types from our email and reestablish it as a list in emailsFiltered
emailsFiltered = list(filter(None, emails))
# We also don't need the column name, it isn't an email.
emailsFiltered.remove('Email Address')

### Last, we print to the command line what we have.
print('Emails found in responses:')
for i in emailsFiltered:
    print(i)