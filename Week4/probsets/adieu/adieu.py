import inflect

p = inflect.engine()

names = []

while True:
    try:
        user_input = input("Name: ")
        names.append(user_input)
    except EOFError:
        break
print()
print("Adieu, adieu, to", p.join(names))


# count = 2

# print("There", p.plural_verb("was", count), p.number_to_words(count), p.plural_noun("person", count), "by the door.")
