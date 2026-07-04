def main():
    expression = input("Expression: ").split()
    number1, operator, number2 = expression.split()
    number1 = float(number1)
    number2 = float(number2)


    if operator == "+":
        results = number1 + number2
        print(results)
    elif operator == "-":
        results = number1 - number2
        print(results)
    elif operator == "/":
        results = number1 / number2
        print(results)
    elif operator == "*":
        results = number1 * number2
        print(results)
    else:
        print("Invalid input")
main()



