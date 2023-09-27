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

# Main function to take user input and perform calculations
def calculator():
    while True:
        print("\nSIMPLE CALCULATOR")
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'subtract' for subtraction")
        print("Enter 'multiply' for multiplication")
        print("Enter 'divide' for division")
        print("Enter 'quit' to exit")
        
        choice = input("Enter your choice: ")
        
        if choice == 'quit':
            break
        
        if choice in ('add', 'subtract', 'multiply', 'divide'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == 'add':
                result = add(num1, num2)
                print("Result: ", result)
            elif choice == 'subtract':
                result = subtract(num1, num2)
                print("Result: ", result)
            elif choice == 'multiply':
                result = multiply(num1, num2)
                print("Result: ", result)
            elif choice == 'divide':
                result = divide(num1, num2)
                print("Result: ", result)
        else:
            print("Invalid input. Please try again.")

# Run the calculator
calculator()
