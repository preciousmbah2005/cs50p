import random

def main():
    chosen_level = get_level()



def get_level():
    random_list = [1, 2, 3]

    while True:
        try:
            prompt = int(input("Level: "))

            if prompt in random_list:
                return 
            
        except ValueError:
                continue
    


def generate_integer(level):
    correct_count = 0
    wrong_count = 0
    trial = 0

    while correct_count < 10:
        X = random.randint(1, 10)
        Y = random.randint(1, 10)
        correct_answer = X + Y

        while True:
            user_answer = int(input(f"{X} + {Y} = "))

            if user_answer == correct_answer:
                    correct_count += 1
                    trial += 1
                    return
            else:
                wrong_count += 1
                print("EEE")

                if wrong_count == 3:
                    print(f"{X} + {Y} = {correct_answer}")
                    wrong_count = 0
                    trial -= 1
                    return
            
print(f"Score:  {trial}")       


if __name__ == "__main__":
    main()