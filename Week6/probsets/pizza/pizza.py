import sys
import csv
from tabulate import tabulate


if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few comman-line arguments")

file_name = sys.argv[1]

if not file_name.lower().endswith(".csv"):
    sys.exit("Not a CSV file")


try:
    with (
        open("regular.csv", newline='') as file1,
        open("sicilian.csv", newline='') as file2
        ):
        if file_name == "regular.csv":
            csv_reader_one = csv.reader(file1)
            for line in csv_reader_one:
                print(tabulate(csv_reader_one, tablefmt="grid"))
            
        elif file_name == "sicilian.csv":
            csv_reader_two = csv.reader(file2)
            for line in csv_reader_two:
                    print(tabulate(csv_reader_two, tablefmt="grid"))

except FileNotFoundError:
    sys.exit("Not a CSV file")




   
