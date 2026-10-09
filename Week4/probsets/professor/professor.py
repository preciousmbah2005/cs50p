import random

random_list = [1, 2, 3]

while True:
    try:
        prompt = int(input("Level: "))

        if prompt in random_list:
            break

    except ValueError:
        continue

while True:
    X = random.randint(1, 10)
    Y = random.randint(1, 10)
    correct_answer = X + Y
    user_answer = int(input(f"{X} + {Y} = "))
    if user_answer == correct_answer:
        continue
    else:
        print("EEE")

