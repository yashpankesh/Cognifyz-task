'''Task: Fibonacci Sequence

Write a Python function that generates the Fibonacci sequence up to a given number of terms. The function should
take an integer input from the user and display the Fibonacci sequence up to that number of terms.'''

def generate_fibonacci(n):
    # Check if the input is valid
    if n <= 0:
        return "Please enter a positive integer."

    # Handle cases with 1 or 2 terms
    if n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    # Generate the Fibonacci sequence
    sequence = [0, 1]
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    return sequence

# Get user input
try:
    terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
    result = generate_fibonacci(terms)
    print("Fibonacci Sequence:", result)
except ValueError:
    print("Invalid input! Please enter an integer.")
