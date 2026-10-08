import random


while True:
    try:
        user_input = int(input("Level: "))
        num = random.randint(1, 10000)

        if user_input > 0:
            break
        else:
            continue
    except ValueError:
        continue

while True:
    try:
        guess = int(input("Guess: "))
        if guess == num:
            print("Just right!")
        elif guess > num:
            print("Too large!")
        else:
            print("To small!")
    except ValueError:
        continue