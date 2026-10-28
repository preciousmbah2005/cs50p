import csv
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    before_file_name = sys.argv[1]
    after_file_name = sys.argv[2]

    students = []

    try:
        with open(before_file_name) as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                last, first = row["name"].strip().split(", ")
                students.append({
                    "first": first.strip(),
                    "last": last.strip(),
                    "house": row["house"],
                })
    except FileNotFoundError:
        sys.exit(f"Could not read {before_file_name}")

    with open(after_file_name, "w") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
        writer.writeheader()
        writer.writerows(students)


if __name__ == "__main__":
    main()
