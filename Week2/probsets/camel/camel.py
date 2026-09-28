mixed_case = input("Enter a camel Case variable name: ")

snake_case = ""

for letter in mixed_case:
        if letter.isupper():
                snake_case += "_" + letter.lower()
        else:
                snake_case += letter
print(f"snake case: {snake_case}")

