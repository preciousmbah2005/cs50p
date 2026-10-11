import random

def main():
    chosen_level = get_level()
    generated_level = generate_integer(chosen_level)

    score = 0
    trail = 0
    wrong_count = 0

    while score < 10:
        X = generate_integer(chosen_level)
        Y = generate_integer(chosen_level)
        correct_answer = X + Y

        while True:
            user_answer = int(input(f"{X} + {Y} = "))

            if user_answer == correct_answer:
                score += 1
                trail += 1
                break


            else:
                wrong_count += 1
                print("EEE")

                if wrong_count == 3:
                    print(f"{X} + {Y} = {correct_answer}")
                    score += 0
                    break

    print(f"Score: {trail}")

    # wrong_count = 0
    # trial = 0

    # while True:
    #     user_answer = int(input(f"{X} + {Y} = "))

    #     if user_answer == correct_answer:
    #             level += 1
    #             trial += 1
    #             break

    #     else:
    #         wrong_count += 1
    #         print("EEE")

    #         if wrong_count == 3:
    #             print(f"{X} + {Y} = {correct_answer}")
    #             wrong_count = 0
    #             break


    # print(f"Score:  {trial}")



def get_level():
    random_list = [1, 2, 3]

    while True:
        try:
            prompt = int(input("Level: "))

            if prompt in random_list:
                return prompt

        except ValueError:
                continue



def generate_integer(level):

    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
         return random.randint(100, 999)
    else:
         raise ValueError


if __name__ == "__main__":
    main()
