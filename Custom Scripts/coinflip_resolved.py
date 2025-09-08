import random

guess = ''

toss = random.randint(0, 1) #assigns heads or tail in a range of 0 to 1...

match toss: #Converts the numeric value into string heads or tails to match.
    case 0:
        toss = 'tails'
    case 1:
        toss = 'heads'

#Guess 1
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter "heads" or "tails":')
    guess = input()
    guess = guess.lower()

if toss == guess:#Pass
    print('You got it!')
    quit()

else: #Fail, retry
    print('Nope! Guess again!')
    guess = ''

#Guess 2
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter "heads" or "tails":')
    guess = input()
    guess = guess.lower()

if toss == guess: #Pass
    print('You got it!')
    quit()

else: #Fail
    print('Nope. You are really bad at this game.')
    quit()