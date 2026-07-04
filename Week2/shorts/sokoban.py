"""
def main():
    history = []

    while True:
        action = input("Action: ").title().strip()

        if action == "Undo":
            undone = history.pop()
            print(f"Undone: {undone}")
        elif action == "Restart":
            history.clear()
        else:
            history.append(action)


        print(history)


main()

"""

def main():
    history = []

    while True:
        action = input("Action: ").title().strip()

        if action == "Undo":
            if history:  # Safety check: make sure history isn't empty
                removed_item = history.pop()  # Removes and returns the LAST item
                print(f"Undid action: {removed_item}")
                print(f"Updated list: {history}")
            else:
                print("Nothing to undo!")

            # STOPS here and goes back to the top of the loop
            continue

        # This only runs if the action was NOT "undo"
        history.append(action)
        print(history)

main()
