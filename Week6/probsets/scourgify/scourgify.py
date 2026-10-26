import csv
import sys

# Validate commmand-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many comman-line arguments")

before_file_name = sys.argv[1]
after_file_name = sys.argv[2]

# Ensure I am dealing with CSV file
if not before_file_name.endswith(".csv") or not after_file_name.endswith(".csv"):
    sys.exit("Not a CSV file")

converted_data = []

try:
    # Open both files using a tuple
    with (
        open(before_file_name, mode="r", newline="") as infile,
        open(after_file_name, mode="w", newline="") as outfile,
        ):

    # Read the file and update datastructure 'converted_data'
        if before_file_name == "before.csv":
            reader = csv.DictReader(infile)
            for row in reader:
                first, last = row["name"].strip().split(", ")

                # Append the newly formatted dictionary to the list
                converted_data.append({
                    "first":  first.strip(),
                    "last": last.strip(),
                    "house": row["house"]
                })

    # Write the transformed data to the target file
        if after_file_name == "after.csv":
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(converted_data)

except FileNotFoundError:
    sys.exit("Input file does not exist")         
                