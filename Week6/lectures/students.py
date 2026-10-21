import csv

"""Writing files"""
name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})


"""Reading files"""
# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})
#         student.append(row)
#     # for line in file:
#     #     name, home = line.rstrip().split(",")
#     #     student = {"name": name, "home": home}
#     #     students.append(student)


# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['home']}")

