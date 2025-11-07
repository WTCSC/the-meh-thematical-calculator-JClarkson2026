"""
calculator.py
-------------
A sarcastic and intentionally rude command-line calculator program.

This script performs basic arithmetic operations (+, -, *, /)
and provides humorous (and mildly insulting) responses for user input errors.

"""

def add(a, b):
    """
    Adds two numbers.

    Parameters:
        a (int or float): The first operand.
        b (int or float): The second operand.

    Returns:
        int or float: The sum of `a` and `b`.
    """
    return a + b


def subtract(a, b):
    """
    Subtracts one number from another.

    Parameters:
        a (int or float): The number to subtract from.
        b (int or float): The number to subtract.

    Returns:
        int or float: The result of `a - b`.
    """
    return a - b


def multiply(a, b):
    """
    Multiplies two numbers.

    Parameters:
        a (int or float): The first operand.
        b (int or float): The second operand.

    Returns:
        int or float: The product of `a` and `b`.
    """
    return a * b


def divide(a, b):
    """
    Divides one number by another, with special handling for division by zero.

    Parameters:
        a (int or float): The numerator.
        b (int or float): The denominator.

    Returns:
        int, float, or str:
            - The quotient of `a / b` if `b` is not zero.
            - A humorous error message if division by zero is attempted.
    """
    if b == 0:
        # Handle division by zero with a snarky comment.
        return "wow... you're such an incredibley smart person, I bet your dad is proud of you"
    return a / b


def run():
    """
    Runs the interactive calculator session.

    Prompts the user for two numbers and an arithmetic operation.
    Performs the requested operation and prints the result or
    a custom error message for invalid input.

    Notes:
        - Input is taken as a string and converted to an integer.
        - Invalid conversions (non-numeric input) will raise an exception
          if not handled, though this code assumes basic user compliance.
    """
    print("welcome to the calculator program... bc you couldn't do it yourself depsite it being basic math.")

    # Prompt user for the first number
    numberOne = input("what's your first number you seal? ")
    # Check if the input can be converted to an integer; if not, mock the user.
    try:
        int(numberOne)
    except ValueError:
        print("wow... you're such an incredibley smart person, I bet your dad is proud of you")

    # Prompt user for the second number
    numberTwo = input("what's your second number you big brainer? ")
    try:
        int(numberTwo)
    except ValueError:
        print("wow... you're such an incredibley smart person, I bet your dad is proud of you")

    # Ask for the arithmetic operation
    operation = input("now listen... + - * / nothing else you go this... ")

    # Select and execute the correct arithmetic operation based on user input
    if operation == "+":
        print(add(int(numberOne), int(numberTwo)))
    elif operation == "-":
        print(subtract(int(numberOne), int(numberTwo)))
    elif operation == "*":
        print(multiply(int(numberOne), int(numberTwo)))
    elif operation == "/":
        print(divide(int(numberOne), int(numberTwo)))
    else:
        # Catch invalid operation input with a mocking message
        print("wow... you're such an incredibley smart person, I bet your dad is proud of you")


if __name__ == "__main__":
    # Run the calculator only if this file is executed directly,
    # not when imported as a module.
    run()
