print("WOOO BASIC CALCULATOR PROGRAM!\nIt can only support 2 numbers and 1 operator.")

user_number1 = input("Number 1: ")
user_number2 = input("Number 2: ")
user_operator = input("Operator: ")

if user_operator == "*":
    print(int(user_number1) * int(user_number2))

if user_operator == "%":
    print(int(user_number1) % int(user_number2))

if user_operator == "+":
    print(int(user_number1) + int(user_number2))

if user_operator == "-":
    print(int(user_number1) - int(user_number2))