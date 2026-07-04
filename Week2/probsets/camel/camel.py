mixed_case = input("camelCase: ")

snake_case = ""

for letter in mixed_case:
        if letter.isupper():
                snake_case += "_" + letter
        else:
                snake_case += letter
print(f"snake case: {snake_case}")

