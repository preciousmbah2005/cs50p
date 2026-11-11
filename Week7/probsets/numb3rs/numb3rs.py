
import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    pattern = r"^(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)$"

    return bool(re.search(pattern, ip))

    # parts = ip.split(".")

    # if len(parts) != 4:
    #     return False

    # for num in parts:
    #     if not num.isdigit():
    #         return False

    #     number = int(num)

    #     if not 0 <= number <= 255:
    #         return False

    #     if len(num) > 1 and num.startswith("0"):
    #         return False

    # return True


if __name__ == "__main__":
    main()
