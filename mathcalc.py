def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        return "wow... you're such an incredibley smart person, I bet your dad is proud of you"
    return a / b

def run():
    print("welcome to the calculator program... bc you couldn't do it yourself depsite it being basic math.")
    numberOne = input("what's your first number you seal? ")
    if not int(numberOne):
        print("wow... you're such an incredibley smart person, I bet your dad is proud of you")
    numberTwo = input("what's your second number you big brainer? ")
    if not int(numberTwo):
        print("wow... you're such an incredibley smart person, I bet your dad is proud of you")
    operation = input("now listen... + - * / nothing else you go this... ")
    if operation == "+":
        print(add(int(numberOne), int(numberTwo)))
    elif operation == "-":
        print(subtract(int(numberOne), int(numberTwo)))
    elif operation == "*":
        print(multiply(int(numberOne), int(numberTwo)))
    elif operation == "/":
        print(divide(int(numberOne), int(numberTwo)))
    else:
        print("wow... you're such an incredibley smart person, I bet your dad is proud of you")

if __name__ == "__main__":
    run()