import random

random_list = [1, 2, 3]

while True:
    try:
        prompt = int(input("Level: "))

        if prompt in random_list:
            break

    except ValueError:
        continue

correct_count = 0
wrong_count = 0

while correct_count < 10:
    X = random.randint(1, 10)
    Y = random.randint(1, 10)
    correct_answer = X + Y

    while True:
        user_answer = int(input(f"{X} + {Y} = "))

        if user_answer == correct_answer:
                correct_count += 1
                print(f"Score:  {correct_count}")
                break
        else:
            wrong_count += 1
            print("EEE")

            if wrong_count == 3:
                print(f"{X} + {Y} = {correct_answer}")
                wrong_count = 1
                break
            
            


