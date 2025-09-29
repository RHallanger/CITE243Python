"""
===========================================================
Program Name: The Great File Escape
Author: Robert Hallanger
Date: 2025-09-29
Description:
    This program creates and organizes 100 spam.txt files in a series of folders contained in /spam.
    It is designed to demonstrate my understandings of file organization code and modules in Python.
    
Usage:
    Run the script using Python 3.13. Ensure all dependencies
    are installed before execution.

    Uh oh, you have a spam bug infestation.
    You must find the queen bug or the key file.
    Once you have that, move it to the /spam/key directory like a true exterminator would.

    I hope you aren't byting off more than you can compile.
    Okay, enough awful and forced puns, have fun.

===========================================================
"""
import random
import shutil
import os
from pathlib import Path

### Part 1: MAKE RANDOM FOLDERS & FILES
home = Path.home()
# Creates folder spam and key
(home/'spam/key').mkdir(exist_ok=True,parents=True)
# Creates a random amount of folders under /home/spam
for i in range(random.randint(1,50)):
    (home/f'spam/{i}').mkdir(exist_ok=True)
    print('Folder -' + home + f'/spam/{i} - has been created')
    # Creates a random amount of text files in each {i} folder
    for j in range(random.int(3)):
        with open(home/f'spam/{i}/{j}_file.txt', 'w') as file:
            file.write('Hey kid, I\'m just a busy working file.\nThe queen file is probably in a different folder.')
        print(f'File - {j}_file.txt in ' + home + f'/spam/{i}')

### Part 2: MAKE THE KEY
# I need a random checker to verify that a {i} folder exists and add the key into it,
# it needs to be random or else it wouldn't be fun.
keyFolder = (home/'spam'/str(random.int(1,50)))
# This will keep re-rolling what folder to check until it finds a created folder
while not keyFolder.exists():
    keyFolder = (home/'spam'/str(random.int(1,50)))
print(keyFolder + ' has been selected to host the key.')
keyText = 'Ohhh dear, you hath foundeth me and my queenly .txt contents.\nAs the ruler of the spam files, please do not put me in the /spam/key folder.'
# We have found a random folder to implement the key into
with open (keyFolder/'QueenFile.txt', 'w'):
    file.write(keyText)
print('QueenFile.txt has been created in key folder.')

### Part 3: CHECK FOR KEY
while (not (home/'spam/key/QueenFile.txt').exists()) and ((home/'spam/key/QueenFile.txt') != keyText):
    input('QueenFile.Txt is not detected or has improper contents.\nPress enter to continue...')

print('You have removed the queen.')
### Part 4: Delete spam files
# for folder, file in os.walk(home/'spam'):
#     print('')