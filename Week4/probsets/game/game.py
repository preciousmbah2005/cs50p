import random

while True:
    try:
        user_input = int(input("Level: "))

        if user_input <= 0:
            continue

    except ValueError:
        continue
    break

num = random.randint(1, user_input)

while True:
    try:
        guess = int(input("Guess: "))

        if guess > 0:
            if guess == num:
                print("Just right!")
                break
            elif guess > num:
                print("Too large!")
            else:
                print("Too small!")
        else:
            continue

    except ValueError:
        continue


