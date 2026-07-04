def main():

    # Getting user's input
    value = int(input("Enter a number: "))

    # Conditions to know if value is even or not
    if even_number(value):
        print("This is an even number")
    else:
        print("This is an odd number")



# Creating a better and succinct code
def even_number(num):
    return num % 2 == 0

"""
# And alternative
def even_number(num):
    return True if num % 2 == 0 else False

"""

"""
# Creating my own function if it's even or not
def even_number(num):
    if num % 2 == 0:
        return True
    else:
        return False

"""


main()

