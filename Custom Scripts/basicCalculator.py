print("WOOO BASIC CALCULATOR PROGRAM!\nIt can only support 2 numbers and 1 operator.")

try:
    user_number1 = int(input("Number 1: "))
    user_number2 = int(input("Number 2: "))

except:
    print('Exception found, did you not use a number?')
    quit()
    
user_operator = input("Operator: ")

if user_operator == "*":
    print(user_number1 * user_number2)

elif user_operator == "/":
    print(user_number1 / user_number2)

elif user_operator == "+":
    print(user_number1 + user_number2)

elif user_operator == "-":
    print(user_number1 - user_number2)

else:
    print('I can't do that.')
