import random

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
    guess = guess.lower()

toss = random.randint(0, 1)  # 0 is tails, 1 is heads

if toss == 0:
    toss = 'tails'
else:
    toss = 'heads'

if toss == guess:
    print('You got it!')

else:
    print('Nope! Guess again!')
    guess = input()
    guess = guess.lower()

    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')