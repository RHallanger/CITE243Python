#Collatz performs the functions to reduce a number to 1
def collatz(number):
    print(f' {number} ')
    if number % 2 == 0: #If the number is a factor of 2, divide by 2
        number = number // 2
        collatz(number)
    elif number == 1: #If the number is 1, tell them it has reached 1.
        print('The final result is 1.')
        userNum = 0
        userInputLoop()
    else: #If the number isn't 1 and not a factor of 2, then multiply by 3 and add 1.
        number = 3 * number + 1
        collatz(number)

#Puts the user into a loop to either get a number or tell them that their entry isn't valid.
def userInputLoop():
    global userNum
    try:
        userNum = int(input('Enter a number: '))
        collatz(userNum)

    except:
        print('That isn\'t a valid number...')
        userInputLoop()

#Start of the actual script.
userNum = 0
userInputLoop()