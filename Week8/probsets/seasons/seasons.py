
import sys
import inflect
from datetime import date


def main():
    birth_date = input("Date of Birth: ")

    try:
        minutes = calculate_minutes(birth_date)
    except ValueError:
        sys.exit("Invalid input")

    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    print(f"{words.capitalize()} minutes")


def calculate_minutes(birth_date, today=None):
    birthday = date.fromisoformat(birth_date)

    if today is None:
        today = date.today()

    difference = today - birthday
    return difference.days * 24 * 60


if __name__ == "__main__":
    main()
