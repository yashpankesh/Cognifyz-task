'''Task: Password Strength Checker

Create a Python function that evaluates the strength of a password entered by the user. Implement checks for 
factors such as length, presence of uppercase and lowercase letters, digits, and special characters.'''

import re

def password_strength_checker(password):
    # Check password length
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    
    # Check for lowercase letters
    if not re.search("[a-z]", password):
        return "Weak: Password must contain at least one lowercase letter."
    
    # Check for uppercase letters
    if not re.search("[A-Z]", password):
        return "Weak: Password must contain at least one uppercase letter."
    
    # Check for digits
    if not re.search("[0-9]", password):
        return "Weak: Password must contain at least one digit."
    
    # Check for special characters
    if not re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak: Password must contain at least one special character."
    
    # If all checks passed
    return "Strong: Password is strong."

# Get password input from the user
password = input("Enter a password to check its strength: ")
strength = password_strength_checker(password)
print(strength)
