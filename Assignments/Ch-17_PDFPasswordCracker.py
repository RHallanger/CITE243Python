"""
===========================================================
Program Name: Password Cracker
Author: Robert Hallanger
Date: 2025-10-27
Description:
This program performs a basic dictionary list loader to decrypt a word
document.
It is designed to crack passwords on a word document.
Usage:
Run the script using Python 3.13. Ensure all dependencies
are installed before execution.
===========================================================
"""
from pathlib import Path
import msoffcrypto
import io
import os
from docx import Document

pdfPath = input('Paste a PDF file path that you want to crack: ').strip()
wordlist = input('Paste a wordlist file path (Leave blank for default): ').strip()
i = 1 #Counter for the line currently on
b = 0 # Intialize total lines in wordlist

if wordlist == '':
    wordlist = 'Misc Resources/dictionary.txt'

for a in open(wordlist, 'r'):
    b += 1

encrypted = open(pdfPath, 'rb')
file = msoffcrypto.OfficeFile(encrypted)
if not file.is_encrypted():
    print('The DOCX file is not password protected.')
    exit()
print('File is encrypted. Beginning password cracking...')

for a in open(wordlist, 'r'):
    print(f'Trying password: {a} ({i}/{b})')
    file.load_key(password=a.strip())
    try:
        decrypted = io.BytesIO()
        file.decrypt(decrypted)
        print(f'\nPassword found: {a.strip()}')
        break
    except:
        pass
    file.load_key(password=a.strip().upper())
    try:
        decrypted = io.BytesIO()
        file.decrypt(decrypted)
        print(f'\nPassword found: {a.strip().upper()}')
        break
    except:
        pass
        i += 1
input()
