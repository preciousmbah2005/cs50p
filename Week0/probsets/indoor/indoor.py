# The main function that returns the input
def main():
    text = input("")
    print(f"{lower_case(text)}")

# A custom function that makes text lower case
def lower_case(text):
    return text.lower()


main()
