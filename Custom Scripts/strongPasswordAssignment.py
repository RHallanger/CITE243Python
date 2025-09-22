import re

'''
Password rules:
- Must have 8 or more characters included.
- Must contain an uppercase and a lowercase character.
- At least 1 digit
- At least 1 special character
'''

attempts = 0

def cli(text):
    print('Non-USG_System' + text)

def newPassLoop():
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
    password = input('Non-USG_System (New Password)> ')
    password = password.strip()
    specCheck = specials.findall(password)
    digCheck = digits.findall(password)
    upperCheck = uppers.findall(password)
    lowerCheck = lowers.findall(password)
    if len(password) < 8:
        cli('> Password must be 8 or more characters.')
    print(specCheck)
    print(digCheck)
    print(upperCheck)
    print(lowerCheck)


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
username = input('Non-USG_System (Username)> ')
while (username == 'admin') or (username == 'administrator'):
    if attempts < 3:
        input('Non-USG_System (Password)> ')
        print('Non-USG_System> The password you entered is incorrect! You have ' + str(3 - attempts) + ' attempts until the account is locked.')
        attempts += 1
    else:
        input('Non-USG_System> ' + username + ' has been locked. Please contact your system administrator.')
cli('> Account not registered in database.')
cli('> Creating a new account.')
newPassLoop()
