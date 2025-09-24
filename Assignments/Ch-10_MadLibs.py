"""
===========================================================
Program Name: Mad Libs Program
Author: Robert Hallanger
Date: 2025-09-23
Description:
    This program performs a basic substitution of words in a sentence.
    It is designed to entertain.
    
Usage:
    Run the script using Python 3.13. Ensure all dependencies
    are installed before execution.

===========================================================
"""

'''
How to use this program:
User will enter data into madlib_prompt.txt
With ADJECTIVE, NOUN, and VERB used to key
the program to prompt users for input then
creates madlib_output.txt with the changes.

madlib_prompt.txt must be present in the same
folder as this program.

IE:
The ADJECTIVE panda walked to the NOUN and then VERB. 
A nearby NOUN was unaffected by these events.
'''

######### Libraries
from pathlib import Path
import os
import re

######### Variables
option = ''
newWord = ''
outputList = []

### This will verify that madlib_prompt.txt is reachable
madFile = Path(Path.cwd()/'madlib_prompt.txt')
### If madlib_prompt.txt can't be found it will create the file and add instructions inside of there and prompts the user to read that file before re-executing this file.
if not madFile.is_file():
    print('Program could not find madlip_prompt.txt in ' + str(Path.cwd()))
    with open('madlib_prompt.txt', 'w') as file:
        file.write('''
How to use this program:
Enter a prompt with ADJECTIVE, NOUN, and VERB.
These terms are used to tell the program to prompt users for relevant inputs.

When you execute the program with this file present, it will
create a madlib_output.txt here in the same folder.

EXAMPLE:
The ADJECTIVE panda walked to the NOUN and then VERB. 
A nearby NOUN was unaffected by these events.
''')
    print('Creating a blank madlib_prompt.txt in ' + str(Path.cwd()) + '...')
    input('Be sure to open the new file and read the instructions within it.')
    quit()
### Otherwise madlib_prompt.txt is present so we will just use what we found in it...
else:
    with open('madlib_prompt.txt') as file:
        madData = file.read()


### This part took me a while to get right.
### Since madData comes in as a single string with the .read() function, we will seperate it into a list for each word.
col = madData.split(' ')
### Now that col is a list of every word in the prompt, we will loop through each word looking to see if it contains what we are looking for and replace only the flag.
for item in col:
    if 'NOUN' in item:
        newWord = input('Enter a noun: ')
        item = item.replace('NOUN', newWord)
    elif 'VERB' in item:
        newWord = input('Enter a verb: ')
        item = item.replace('VERB', newWord)
    elif 'ADJECTIVE' in item:
        newWord = input('Enter an adjective: ')
        item = item.replace('ADJECTIVE', newWord)
    ### We are making a new list since working with col afterwards was becoming a hassle.
    outputList.append(item)

### With outputList assembled, we need to convert it back into a string.
madLib = ' '.join(outputList)
print('\n' + madLib)

### Now creating an output file as to not touch the user's prompt in case they should want to reuse it.
### If madlib_output.txt already exists, we will prompt the user to verify if they want it to be overwritten or if they would like to quit the program to rename their last outputted prompt.
madOut = Path(Path.cwd()/'madlib_output.txt')
if madOut.is_file():
    while option not in ['yes', 'no', 'y', 'n']:
        print('madlib_output.txt is about to be overwritten...')
        print('Would you like to continue?')
        option = input('([Y]es/[N]o): ')
        option = option.lower()
        match option:
            case 'yes':
                with open('madlib_output.txt', 'w') as file:
                    file.write(madLib)
            case 'y':
                with open('madlib_output.txt', 'w') as file:
                    file.write(madLib)
            case 'no':
                input('Closing program, please rename madlib_output.txt before using this program again.')
                quit()
            case 'n':
                input('Closing program, please rename madlib_output.txt before using this program again.')
                quit()
            case _:
                input('User must input "Yes" or "No".')
### Again, the file doesn't exist, so we will just create one.
else:
    with open('madlib_output.txt', 'w') as file:
        file.write(madLib)
    print('Prompt saved to madlib_output.txt')

### Why not just make more files and slap a new number at the end?
### Because it would make the folder messy for a mad libs project.
### I can provide code for that though.
# i = 0
# while madOut.isfile():
#     i += 1
#     madOut = Path(Path.cwd()/f'madlib_output{i}.txt')
# with open(f'madlib_output{i}.txt', 'w') as file:
#     file.write(madLib)