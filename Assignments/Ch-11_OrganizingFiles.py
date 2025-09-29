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
import logging
from pathlib import Path

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable()

### Part 1: MAKE RANDOM FOLDERS & FILES
home = Path.home()
# Creates folder spam and key
(home/'spam/key').mkdir(exist_ok=True,parents=True)
# Creates a random amount of folders under /home/spam (at least 2, up to 11)
for i in range(random.randint(1,10)):
    (home/f'spam/{i}').mkdir(exist_ok=True)
    logging.debug('Folder -' + str(home) + f'/spam/{i} - has been created')
    # Creates a random amount (up to 3) of text files in each {i} folder
    for j in range(random.randint(0, 3)):
        with open(home/f'spam/{i}/{j}_file.txt', 'w') as file:
            file.write('Hey kid, I\'m just a busy working file.\nThe queen file is probably in a different folder.')
        logging.debug(f'File - {j}_file.txt in ' + str(home) + f'/spam/{i}')

### Part 2: MAKE THE KEY
# I need a random checker to verify that a {i} folder exists and add the key into it,
# it needs to be random or else it wouldn't be fun.
keyFolder = (home/'spam'/str(random.randint(1,10)))
# This will keep re-rolling what folder to check until it finds a created folder
while not keyFolder.exists():
    keyFolder = (home/'spam'/str(random.randint(1,10)))
logging.debug(str(keyFolder) + ' has been selected to host the key.')
keyText = 'Ohhh dear, you hath foundeth me and my queenly .txt contents.\nAs the ruler of the spam files, please do not put me in the /spam/key folder.'
# We have found a random folder to implement the key into
with open(keyFolder/'QueenFile.txt', 'w') as file:
    file.write(keyText)
logging.debug('QueenFile.txt has been created in key folder.')

### Part 3: CHECK FOR KEY
print('OH NO, a colony of files has moved into your filesystem at ' + str(home) + '/spam!\nFind the QueenFile.txt and move it to the key folder in spam to relocate the colony.')
while (not (home/'spam/key/QueenFile.txt').exists()) and ((home/'spam/key/QueenFile.txt') != keyText):
    print('\n\n')
    input('QueenFile.txt is not detected or has improper contents.\nPress enter to re-verify the key folder...')

print('\nYou did it!\nYou have removed the queen!\n\nAll of the files are now cleaning up their home and leaving.')
### Part 4: Delete spam files
# First we walk Spam for all of the folders that were generated under it.
for folder_name, subfolders, filenames in os.walk(home/'spam'):
    # Now we recursively walk every folder that was generated and remove the files.
    for subfolder in subfolders:
        for folder_name, subfolders, filenames in os.walk(home/'spam'/subfolder):
            # And then we remove every file in that subfolder
            for file in filenames:
                logging.debug('REMOVING ' + file)
                os.unlink(home/'spam'/subfolder/file)
            logging.debug('REMOVING /' + folder_name)
            os.rmdir(folder_name)
    # And then we remove /spam
    logging.debug('REMOVING /spam')
    os.rmdir(home/'spam')