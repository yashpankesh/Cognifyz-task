'''Task1: Guessing Game

Write a Python program that generates a random number between 1 and 100. The user should then try to guess the 
number.The program should provide hints such as "too high" or "too low" until the correct number is guessed.'''

import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I have picked a random number between 1 and 100.")
    print("Try to guess it! I'll give you hints if you're too high or too low.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0  # To track the number of attempts

    while True:
        try:
            # Ask the user for their guess
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
            print("Invalid input! Please enter a number.")

# Run the guessing game
guessing_game()
