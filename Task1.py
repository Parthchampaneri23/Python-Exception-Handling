#Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

def divide_numbers(a , b):
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Usage
numerator = 100
denominator = 0
divide_numbers(numerator, denominator)
