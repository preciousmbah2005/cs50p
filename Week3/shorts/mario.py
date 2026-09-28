def main():
    while True:
        try:
            user_input = input("Height: ")
            height = int(user_input)
            pyramid(height)
        except ValueError:
            print(f"{user_input} is not a valid interger")
        else:
            break

def pyramid(n):
    for i in range(n):
        print("#" * (1 + 1))


if __name__ == "__main__":
    main()

