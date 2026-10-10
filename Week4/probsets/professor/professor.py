import random

def main():
    chosen_level = get_level()
    generated_level = generate_integer(chosen_level)
    


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
    level = 0
    wrong_count = 0
    trial = 0
        
    

    while level < 10:
        X = random.randint(1, 10)
        Y = random.randint(1, 10)
        correct_answer = X + Y

        while True:
            user_answer = int(input(f"{X} + {Y} = "))

            if user_answer == correct_answer:
                    level += 1
                    trial += 1
                    break
                    
            else:
                wrong_count += 1
                print("EEE")

                if wrong_count == 3:
                    print(f"{X} + {Y} = {correct_answer}")
                    wrong_count = 0
                    trial -= 1
                    break
                    
            
    return print(f"Score:  {trial}")


if __name__ == "__main__":
    main()