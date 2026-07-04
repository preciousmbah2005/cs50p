# calculator.py
# Week 0 - Variables and Functions

def addition(x, y):
    return x + y

def division(x, y):
    return x / y

def main():

    # Ask user for numbers
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    # Perform calculations
    add_result = addition(x, y)
    div_result = division(x, y)

    # Display results
    print(f"Addition: {add_result}")
    print(f"Division: {div_result}")

main()
