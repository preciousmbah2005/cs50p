def main():
    while True:
        try:
            user_fraction = input("Fraction: ")

            X, Y = user_fraction.split("/")
            X = int(X)
            Y = int(Y)

            if X > Y or X < 0:
                continue

            result = round((X / Y) * 100)
            break

        except (ValueError, ZeroDivisionError):
            continue

    if result <= 1:
        print(f"E")
    elif result >= 99:
        print(f"F")
    else:
        print(f"{result}%")


main()

