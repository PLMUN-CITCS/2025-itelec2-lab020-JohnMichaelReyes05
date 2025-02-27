"""
Filename: even_odd_checker_functions.py
This script checks if an entered integer is even or odd using modular functions.
"""

def get_integer_input() -> int:
    """
    Handles user input to obtain a valid integer.
    Repeatedly prompts the user until a valid integer is entered.
    Returns:
        int: The validated integer input from the user.
    """
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    """
    Determines if a given number is even or odd.
    Args:
        number (int): The number to be checked.
    Returns:
        str: A formatted string indicating if the number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

def main():
    """Main program flow."""
    number = get_integer_input()
    result = check_even_odd(number)
    print(result)

if __name__ == "__main__":
    main()
