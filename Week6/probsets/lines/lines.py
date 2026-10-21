import sys
import csv


if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

if not filename.endswith(".py"):
    sys.exit("Not a Python file")

try:
    with open(filename, mode="r") as file:
        if filename.endswith(".py"):
            loc = 0
            for line in file:
                clean_line = line.strip()
                if clean_line and not clean_line.startswith("#"):
                    loc += 1
            print(loc)
        # else:
        #     csv_reader = csv.reader(file)
        #     total_lines = sum(1 for line in file)
        #     print(total_lines)

except FileNotFoundError:
    sys.exit("File does not exist")
