# Calculator project

print("Welcome to the Calculator! This program can perform basic arithmetic operations. Press enter to begin.")

first = float(input("Enter the first number: "))

second = float(input("Enter the second number: "))

action = input("Enter the operation you want to perform (+, -, *, /): ")

if acion == "+":
    result = first + second

elif action == "-":
    result = first - second

elif action == "*":
    result = first * second

elif action == "/":
    if second == 0:
        print("Error: Division by zero is not allowed.")
        exit()
    result = first / second

else:
    print("Invalid operation. Please use one of the following: +, -, *, /")
    exit()

print(f"The result of {first} {action} {second} is: {result}")



