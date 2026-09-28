menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}



def main():
    # Initializing the variable
    total = 0.0

    while True:
            try:
                prompt = input("Item: ").title()

                # Checks if the item is in the menu
                if prompt in menu:
                    total += menu[prompt]
                else:
                     continue

            except EOFError:
                 break
            except KeyError:
                 continue

            print(f"Total: ${total:.2f}")


main()
