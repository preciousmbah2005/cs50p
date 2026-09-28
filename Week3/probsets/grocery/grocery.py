def main():
    counter = {}
    while True:
        try:
            user_input = input("").upper()
            if user_input in counter:
                counter[user_input] += 1
            else:
                counter[user_input] = 1

        except EOFError:
            print()
            break

    for user_name in sorted(counter):
        print(counter[user_name], user_name)


main()
