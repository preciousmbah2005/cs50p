def main():
    print_square(4)


# def print_square(size):
#     for i in range(size):
#         print("#" * size)


def print_square(size):

    # For each row in square
    for i in range(size):

        # For each brick in row
        for j in range(size):

            # Print brick
            print("#", end="")

        print()


"""
    print_row(4)


def print_row(width):
        print("#" * width)

"""

"""
    print_column(3)


def print_column(height):
    for _ in range(height):
        # print("#")
        print("#\n" * height, end="")

"""


main()
