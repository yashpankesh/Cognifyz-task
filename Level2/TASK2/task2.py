''' Task: Number Guesser

Create a number guessing game where the program generates a random number between a specified range, and the 
user tries to guess it. Provide feedback to the user if their guess is too high or too low.'''

import random

def number_guesser():
    print("Welcome to the Number Guesser Game!")
    print("Choose a range, and I'll pick a random number within it for you to guess.")
    
    try:
        # Get the range from the user
        lower_bound = int(input("Enter the lower bound of the range: "))
        upper_bound = int(input("Enter the upper bound of the range: "))
        
        if lower_bound >= upper_bound:
            print("Invalid range! The lower bound must be less than the upper bound.")
            return

        # Generate a random number in the specified range
        secret_number = random.randint(lower_bound, upper_bound)
        attempts = 0

        print(f"I've picked a number between {lower_bound} and {upper_bound}. Try to guess it!")

        while True:
            try:
                # Get the user's guess
                guess = int(input("Enter your guess: "))
                attempts += 1

                if guess < secret_number:
                    print("Too low! Try again.")
                elif guess > secret_number:
                    print("Too high! Try again.")
                else:
                    print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
                    break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
    except ValueError:
        print("Invalid range! Please enter numbers only.")

# Run the number guesser game
number_guesser()
