"""
# Using list is to complex to scale
students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slythrin"]

"""

"""
# for student in students:
#     print(student)

# using the len function cuz we don't know the size of the list
for i in range(len(students)):
    print(i + 1, students[i])

"""

"""
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

"""

# Creating a dictionary that has many value pairs that is in a list
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Slytherin", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

# for student in students:
#     print(student["name"], student["house"], student["patronus"], sep=", ")

# for i in students:
#     print(students[0]["name"], students[1]["house"], students[2]["patronus"]

for i, student in enumerate(students):
    print(f"{i} {student["name"]} {student["house"]} {student["patronus"]}")

"""
for student in students:
    print(student, students[student], sep=", ")

"""

"""
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

"""


# students = [
#     {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
#     {"name": "Harry", "house": "Slytherin", "patronus": "Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
#     {"name": "Draco", "house": "Slytherin", "patronus": "None"}
# ]

# print(f"{'No.':<4} {'Name':<12} {'House':<12} {'Patronus'}")
# print("-" * 50)

# for i, student in enumerate(students, start=1):
#     patronus_text = str(student["patronus"])
#     print(f"{i:<4} {student['name']:<12} {student['house']:<12} {patronus_text}")
