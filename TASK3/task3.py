''' 
Task3: Email Validator

Develop a Python function that validates whether a given string is a valid email address. Implement checks for 
the format,including the presence of an "@" symbol and a domain name '''

import re

def validate_email(email):
    
    # Define the email validation regex pattern
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if the email matches the pattern
    if re.match(email_pattern, email):
        return True
    else:
        return False

# Example Usage
if __name__ == "__main__":
    print("Welcome to the Email Validator Program!")
    email_to_check = input("Enter an email address to validate: ").strip()
    
    if validate_email(email_to_check):
        print(f"{email_to_check} is a valid email address.")
    else:
        print(f"{email_to_check} is NOT a valid email address.")
