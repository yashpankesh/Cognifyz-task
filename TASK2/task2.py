''' Task2: Temperature Conversion

Create a Python program that converts temperatures between Celsius and Fahrenheit. Prompt the user to enter a
temperature value and the unit of measurement, and then display the converted temperature. '''

def convert_temp():
    print("Welcome to the Temperature Converter!")
    print("You can convert temperatures between Celsius and Fahrenheit.")
    
    temp_value = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of the temperature (C for Celsius, F for Fahrenheit): ").strip().upper()
    
    # Conversion logic
    if unit == 'C':
        # Celsius to Fahrenheit
        converted_temp = (temp_value * 9/5) + 32
        print(f"{temp_value}°C is equal to {converted_temp:.2f}°F.")
    elif unit == 'F':
        # Fahrenheit to Celsius
        converted_temp = (temp_value - 32) * 5/9
        print(f"{temp_value}°F is equal to {converted_temp:.2f}°C.")
    else:
        
        print("Invalid unit entered. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    print("Thank you for using the Temperature Converter!")


convert_temp()
