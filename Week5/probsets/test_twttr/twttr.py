def main():
    text = input("Input: ")
    print(f"Ouput: {shorten(text)}")


def shorten(word):
    output = ""
    for character in word:
        if character not in "aeiouAEIOU":
            output += character
    return output

if __name__ == "__main__":
    main()
    