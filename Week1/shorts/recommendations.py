def main():
    difficulty = input("Difficult or Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Enter a valid difficulty")
        return

    players = input("Multiplayer or Single-player? ")
    if not (players == "Multiplayer" or players == "Single-player"):
        print("Enter a valid number of players")


# Using nested if and elif statements
    if difficulty == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and players == "Single-player":
        recommend("Klondike")
    elif difficulty == "Casual" and players == "Multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")


"""
# Using match keyword to replace nested if statements
    match (difficulty, players):
        case ("Difficult", "Multiplayer"):
            recommend("Poker")
        case ("Difficult", "Single-player"):
            recommend("Klondike")
        case  ("Casual", "Multiplayer"):
            recommend("Hearts")
        case("Casual", "Single-player"):
            recommend("Clock")
        case _:
            print("Invalid input. Please try again")

"""



# Defining a function that will recommend a game to the user
def recommend(game):
    print("You might like", game)


main()
