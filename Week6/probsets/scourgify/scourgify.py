import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many comman-line arguments")

before_file_name = sys.argv[1]
after_file_name = sys.argv[2]

with (
    open("before.csv") as file1,
    open("after.csv") as file2
):
    csv_reader = csv.DictReader(file1)
    for line in csv_reader:
        print(csv_reader)
