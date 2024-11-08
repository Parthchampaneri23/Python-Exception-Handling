#Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

def get_integer_input():
    user_input = input("Please enter an integer: ")
    try:
        # Attempt to convert the input to an integer
        value = int(user_input)
        print(f"You entered a valid integer: {value}")
        return value
    except ValueError:
        # Raise a ValueError if the conversion fails
        raise ValueError("Invalid input! Please enter a valid integer.")

# Call the function
try:
    get_integer_input()
except ValueError as e:
    print(e)
