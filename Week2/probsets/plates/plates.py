def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# 6 conditions for plate to be valid
def is_valid(s):
    # 1st condition is to check if length is less than 2 and greater than 6 and output false if other wise
    if len(s) < 2 or len(s) > 6:
        return False

    # 2nd condition is to check if the first two letters are letters and output false if otherwise
    first_two = s[0:2]
    if not first_two.isalpha():
        return False

    # 3rd condition is to check if the first digit is 0 and output false if otherwise
    for letter in s:
        if letter.isdigit():
            if letter == "0":
                return False
            break

    # 4th condition is to check if no letter after number
    number_started = False
    for letter in s:
        if letter.isdigit():
            number_started = True

        elif number_started and letter.isalpha():
            return False

    # 5th condition is to check if there's any punctuation
    for letter in s:
        if not letter.isalnum():
            return False


    return True


main()
