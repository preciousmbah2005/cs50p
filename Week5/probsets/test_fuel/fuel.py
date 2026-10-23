def main():
    while True:
        try:
            user_fraction = input("Fraction: ")
            percentage = convert(user_fraction)
            output = gauge(percentage)
            print(output)
            break

        except (ValueError, ZeroDivisionError):
            continue
    

def convert(fraction):
    X, Y = fraction.split("/")
    X = int(X)
    Y = int(Y)

    if Y == 0:
        raise ZeroDivisionError
    
    if X > Y or X < 0:
        raise ValueError
    
    return round((X / Y) * 100)


def gauge(percentage):
    if percentage <= 1:
            return "E"
    elif percentage >= 99:
       return "F"
    else:
       return f"{percentage}%"


if __name__ == "__main__":
    main()

