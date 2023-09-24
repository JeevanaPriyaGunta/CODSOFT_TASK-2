# Simple Calculator in Python

# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# User input
while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")

    choice = input("Enter operation: ")

    if choice == "quit":
        break

    if choice in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "add":
            print("Result: ", add(num1, num2))
        elif choice == "subtract":
            print("Result: ", subtract(num1, num2))
        elif choice == "multiply":
            print("Result: ", multiply(num1, num2))
        elif choice == "divide":
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print("Result: ", result)
        else:
            print("Invalid input")
    else:
        print("Invalid input")