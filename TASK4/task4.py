''' Task4: Calculator Program

Create a Python program that acts as a basic calculator. It should prompt the user to enter two numbers and an 
operator (+ , -, *, /, %), and then display the result of the operation.'''

def calculator():
    print("Welcome to the Basic Calculator!")
    print("Enter two numbers and an operator to perform a calculation.")
    print("Operators: +, -, *, /, %")
    
    try:
        # Get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter an operator (+, -, *, /, %): ")

        # Perform the calculation
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero is not allowed.")
                return
        elif operator == "%":
            if num2 != 0:
                result = num1 % num2
            else:
                print("Error: Modulo by zero is not allowed.")
                return
        else:
            print("Error: Invalid operator.")
            return

        # Display the result
        print(f"The result of {num1} {operator} {num2} is: {result}")

    except ValueError:
        print("Error: Please enter valid numbers.")

# Run the calculator
calculator()
