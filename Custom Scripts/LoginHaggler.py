print('You are accessing a SUPER SECRET government system.\nIdentify yourself!\nViolators will be harassed!')

username = input('Username: ')
username = username.lower()
password = input('Password: ')
password = password.lower()

if username == 'admin' and password == 'password':
    print('Aww you guessed the defaults.\nAccess granted...')
    print('We don\'t have anything here.\n\n\n\n\n\nI lied...')
    exit()

elif username == 'admin':
    print('You got password wrong!\nI mean, you got the password wrong.\nAccess denied!')
    exit()

elif username == 'steve':
    print('Did you hear Steve Jobs died of Ligma? LIGMA BALLS\nAccess denied!')
    exit()

elif username == 'walter':
    print('Is it time to cook?')
    exit()

else:
    print('I got nothing for you.\nAccess denied.')
    quit()