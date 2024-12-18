'''  TASK-1 String Reversal
Create a Python function that takes a string as input and returns the reverse of that string. For example, 
if the input is "hello," the function should return "olleh." '''
def reverse_str(string):
    
    reversed_str = ""
    
    for char in string:
        reversed_str = char + reversed_str
        
    return reversed_str

# Get input string from the user
string = input("Enter a string: ")

# Reverse the string
reversed_str = reverse_str(string)

# Print the reversed string
print("Reversed string:", reversed_str)