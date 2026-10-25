import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many comman-line arguments")

before_file_name = sys.argv[1]
after_file_name = sys.argv[2]

with (
    open(before_file_name) as file1,
    open(after_file_name) as file2,
    ):
    if before_file_name == "before.csv":
        csv_reader = csv.DictReader(file1)
        for line in csv_reader:
            print(line)

    new_list = []

    if after_file_name == "after.csv":
        csv_reader = csv.DictReader(file2)
        for line in csv_reader:
            new_list.append({"first": line["first"], "last": line["last"] , "home": line["home"]})
            
            