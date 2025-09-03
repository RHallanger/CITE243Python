def collatz(number):
    print(f' {number} ')
    if number % 2 == 0:
        number = number // 2
        collatz(number)
    elif number == 1:
        print('The final result is 1.')
        userNum = 0
        userInputLoop()
    else:
        number = 3 * number + 1
        collatz(number)

def userInputLoop():
    global userNum
    try:
        userNum = int(input('Enter a number: '))
        collatz(userNum)

    except:
        print('That isn\'t a valid number...')
        userInputLoop()

userNum = 0
userInputLoop()