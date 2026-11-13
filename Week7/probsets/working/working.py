
import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"([0-9]{1,2})(?::([0-5][0-9]))? (AM|PM) to ([0-9]{1,2})(?::([0-5][0-9]))? (AM|PM)"

    match = re.fullmatch(pattern, s)

    if not match:
        raise ValueError

    start_hour = int(match.group(1))
    start_minute = int(match.group(2) or 0)
    start_period = match.group(3)

    end_hour = int(match.group(4))
    end_minute = int(match.group(5) or 0)
    end_period = match.group(6)

    if not (1 <= start_hour <= 12 and 1 <= end_hour <= 12):
        raise ValueError

    if start_period == "AM":
        start_hour = 0 if start_hour == 12 else start_hour
    else:
        start_hour = 12 if start_hour == 12 else start_hour + 12

    if end_period == "AM":
        end_hour = 0 if end_hour == 12 else end_hour
    else:
        end_hour = 12 if end_hour == 12 else end_hour + 12

    return f"{start_hour:02}:{start_minute:02} to {end_hour:02}:{end_minute:02}"


if __name__ == "__main__":
    main()
