class Students:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    student.house = "Number
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Students(name, house)


if __name__ == "__main__":
    main()

# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# my_dog = Dog("Precious", 21)
# print(my_dog.name)
# print(my_dog.age)

