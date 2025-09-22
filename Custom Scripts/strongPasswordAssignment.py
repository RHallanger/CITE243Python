import re
import getpass

'''
Password rules:
- Must have 8 or more characters included.
- Must contain an uppercase and a lowercase character.
- At least 1 digit
- At least 1 special character
'''

attempts = 0

###cli function is just to ease formating to mimic something like CiscoIOS
def cli(text):
    print('\nNon-USG_System' + text)

###
def usernameLoop():
    global attempts
    username = input('\nNon-USG_System (Username)> ')
    if (username == 'admin') or (username == 'administrator'):
        if attempts < 3:
            getpass.getpass()
            attempts += 1
            print('\nNon-USG_System> The password you entered is incorrect! You have ' + str(3 - attempts) + ' attempts until the account is locked.')
            usernameLoop()
        else:
            print('\nNon-USG_System> ' + username + ' has been locked. Please contact your system administrator.')
            usernameLoop()
    return username

def newPassLoop():
    checkFail = False
    specials = re.compile(r'!|@|#|\$|%|\^|&|\*')
    digits = re.compile(r'\d')
    uppers = re.compile(r'[A-Z]')
    lowers = re.compile(r'[a-z]')
    cli('> User must create a new password with the following rules.')
    print('''
###########################################################
#                  Password Rules                         #
###########################################################
#                                                         #
#  - Must have 8 or more characters included.             #
#                                                         #
#  - Must contain an uppercase and a lowercase character. #
#                                                         #
#  - At least 1 digit. [0 through 9]                      #
#                                                         #
#  - At least 1 special character. [!@#$%^&*]             #
#                                                         #
###########################################################
    ''')
    cli(' (New Password)>')
    password = getpass.getpass('')
    password = password.strip() #removes whitespace from around user entry for sanitzation...
    specCheck = specials.findall(password) #Creates a list of all cases it encounters a special character in password
    digCheck = digits.findall(password) #Creates a list of all cases it encounters a digit in password
    upperCheck = uppers.findall(password) #Creates a list of all uppercase letters in password
    lowerCheck = lowers.findall(password) #creates a list of all lowercase letters in password

    #These will verify each step is completed, if any of these trigger, it will require the user to try again.
    if len(password) < 8:
        cli('> Password must be 8 or more characters.')
        checkFail = True
    if len(upperCheck) < 1:
        cli('> Password must contain at least 1 uppercase letter.')
        checkFail = True
    if len(lowerCheck) < 1:
        cli('> Password must contain at least 1 lowercase letter.')
        checkFail = True
    if len(digCheck) < 1:
        cli('> Password must contain at least 1 digit or number.')
        checkFail = True
    if len(specCheck) < 1:
        cli('> Password must contain at least 1 special character depicted above.')
        checkFail = True
    if checkFail == True:
        getpass.getpass('')
        newPassLoop()
    else:
        print(username + '@Non-USG_System> New password has been accepted...')
        cliSelector()

def cliSelector():
    global username
    commands = [
        'help - View available commands', 
        'quit - Closes the application', 
        'passwd - Change the password'
        ]
    print('\n')
    option = input(username + '@Non-USG_System> ')
    match option:
        case 'help':
            for col in commands:
                print(col)
            cliSelector()
        case 'quit':
            quit()
        case 'passwd':
            newPassLoop()
        case _:
            print('Use \'help\' to see all available commands.')
            cliSelector()

print('''
###############################################################
#                        WARNING!                             #
###############################################################
#                                                             #
# You are accessing a non-US Government System.               #
#                                                             #
# Regardless, we expect you to enter a username and password. #
# If you do not have an account, an account will be provided. #
#                                                             #
###############################################################
''')
username = usernameLoop()
cli('> Account not registered in database.')
cli('> Creating a new account...')
newPassLoop()