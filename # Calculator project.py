# Desmos Replica - Almost =)

print("Welcome to the Desmos Replica! This program can perform arithmetic operations and graphing. Press enter to begin.")
input()

action = input("Do you want to perform arithmetic operations or graphing? (Enter 'arithmetic' or 'graphing'): ")

if action.lower() == "arithmetic":
    print("You have chosen arithmetic operations. Let's proceed.")
    
    operation = input("Enter the operation you want to perform: +,-,/,*,**,//,%, and &: ")

    if operation in ["+", "-", "*", "/", "**", "//", "%", "&"]:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))

        if operation == "+":
            result = first + second

        elif operation == "-":
            result = first - second

        elif operation == "*":
            result = first * second

        elif operation == "/":
            if second == 0:
                print("Error: Division by zero is not allowed.")
                exit()
                result = first / second

        elif operation == "**":
            result = first ** second

        elif operation == "//":
            result = first // second

        elif operation == "%":
            result = first % second

        elif operation == "&":
            result = first & second
        
        else:
            print("Invalid operation. Please use one of the following: +, -, *, /, **, //, %, &")
            exit()
elif action.lower() == "graphing":
    print("This function is able to find the zeros, vertical asymptotes, horizontal asymptotes, and the y-intercept of a rational function. Please enter the function in the form of f(x) = ax^n + bx^(n-1) + ... + k.")
    print("Make sure to use the correct syntax for exponents and coefficients. For example, f(x) = 2x^2 + 3x - 5.")
    
    rat_func = input("Enter the rational function: ")

    action2 = input("Do you want to find the zeros, vertical asymptotes, horizontal asymptotes, holes, or the y-intercept? (Enter 'zeros', 'vertical asymptotes', 'horizontal asymptotes', 'holes',or 'y-intercept'): ")

    import sympy as sp

    x = sp.symbols('x')

    expression = sp.sympify(rat_func.split('=')[1].strip())

    if action2.lower() == "zeros":
        zeros = sp.solve(expression, x)
        print(f"The zeros of the function are: {zeros}")

    elif action2.lower() == "vertical asymptotes":
        vertical_asymptotes = sp.solve(sp.denom(expression), x)
        print(f"The vertical asymptotes of the function are: {vertical_asymptotes}")

    elif action2.lower() == "horizontal asymptotes":
        degree_numerator = sp.degree(sp.numer(expression))
        degree_denominator = sp.degree(sp.denom(expression))

        if degree_numerator < degree_denominator:
            print("The horizontal asymptote is y = 0")
        elif degree_numerator == degree_denominator:
            leading_coefficient_numerator = sp.LC(sp.numer(expression))
            leading_coefficient_denominator = sp.LC(sp.denom(expression))
            horizontal_asymptote = leading_coefficient_numerator / leading_coefficient_denominator
            print(f"The horizontal asymptote is y = {horizontal_asymptote}")
        else:
            print("There is no horizontal asymptote.")

    elif action2.lower() == "y-intercept":
        y_intercept = expression.subs(x, 0)
        print(f"The y-intercept of the function is: {y_intercept}")

    elif action2.lower() == "holes":
        holes = sp.solve(sp.numer(expression), x)
        print(f"The holes of the function are: {holes}")

    else:
        print("Invalid action. Please choose from 'zeros', 'vertical asymptotes', 'horizontal asymptotes', 'holes', or 'y-intercept'.")
