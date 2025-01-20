''' Task5: Palindrome Checker

Write a Python function that checks whether a given string is a palindrome. A palindrome is a word, phrase, or 
sequence that reads the same backward as forward (e.g.,"madam" or "racecar").'''

def is_palindrome(string):
    # Remove spaces and convert the string to lowercase for uniformity
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    return cleaned_string == cleaned_string[::-1]

def palindrome_checker():
    while True:
        # Prompt the user for input
        test_string = input("Enter a string to check if it's a palindrome (or type 'exit' to quit): ")
        
        if test_string.lower() == "exit":
            print("Goodbye!")
            break  # Exit the loop if the user types 'exit'

        if is_palindrome(test_string):
            print(f'"{test_string}" is a palindrome!')
        else:
            print(f'"{test_string}" is not a palindrome.')

# Run the program
palindrome_checker()
