import random

print("The NUMBER Game")
try:
    lownum_str = input("Lowest Number>")
    highnum_str = input("Highest Number>")
    attempts_str = input("Amount of Attempts>")

    lownum_int = int(lownum_str)
    highnum_int = int(highnum_str)
    attempts_int = int(attempts_str)

except ValueError:
    print("Input not supported")
    exit

except TypeError:
    print("Input not supported")
    exit

except Exception as e:
    print(f"An unexpected error has occured: {e}")
    exit

if ((lownum_int < 0) or (highnum_int <= lownum_int) or (attempts_int <= 0)):
    print("Invalid values presented")
    exit

answer = random.randint(lownum_int, highnum_int)

while attempts_int > 0:
    attempts_int -= 1
    user_guess = input(f"Attempt ({attempts_int+1}/{attempts_str}):")

    if int(user_guess) == answer:
        print(f"!!!!!!!!!!!!!!!!!!You got it!!!!!!!!!!!!!!!\nAnswer: {str(answer)}\nRange: {lownum_str} - {highnum_str}\nAttempts: {str(int(attempts_str)-attempts_int)}")
        exit
    if int(user_guess) > answer:
        print("TOO HIGH!")
    if int(user_guess) < answer:
        print("TOO LOW!")

if attempts_int <= 0:
    print(f"You did not find {str(answer)} in {attempts_str} tries...")
    exit