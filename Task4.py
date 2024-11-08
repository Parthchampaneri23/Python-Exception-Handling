#Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

def get_number(prompt):
    user_input = input(prompt)
    try:
        # Attempt to convert input to float
        return float(user_input)
    except ValueError:
        # Raise TypeError if conversion fails
        raise TypeError("Input must be a numerical value.")

def main():
    try:
        # Get two numbers from the user
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        
        # If successful, print the numbers
        print(f"You entered: {num1} and {num2}")
    except TypeError as e:
        print(e)

if __name__ == "__main__":
    main()
