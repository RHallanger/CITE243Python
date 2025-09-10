import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable()

#Collatz performs the functions to reduce a number to 1
def collatz(number):
    print(number)
    if number <= 0:
        print(str(number) + ' is not a parseable whole number.')
        userNum = 0
        userInputLoop()
    if number % 2 == 0: #If the number is a factor of 2, divide by 2
        logging.debug('UserNum is a factorial of 2.')
        number = number // 2
        collatz(number)
    elif number == 1: #If the number is 1, tell them it has reached 1.
        logging.debug('UserNum has evaluated to 1.')
        print('The final result is 1.')
        userNum = 0
        userInputLoop()
    else: #If the number isn't 1 and not a factor of 2, then multiply by 3 and add 1.
        logging.debug('UserNum is neither a factorial of 2 or equal to 1.')
        number = 3 * number + 1
        collatz(number)

#Puts the user into a loop to either get a number or tell them that their entry isn't valid.
def userInputLoop():
    global userNum
    try:
        userNum = int(input('Enter a whole number: '))
        collatz(userNum)

    except:
        print('That isn\'t a valid number...')
        userInputLoop()

    logging.debug('User has entered: ' + str(userNum))


#Start of the actual script.
userNum = 0
userInputLoop()