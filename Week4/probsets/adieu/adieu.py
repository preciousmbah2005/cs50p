import inflect

p = inflect.engine()

# while True:
#     try:
#         user_input = input("Name: ")
#     except EOFError:
#         print(f"Adieu, adieu to {user_input}")
#         break

count = 2

print("There", p.plural_verb("was", count), p.number_to_words(count), p.plural_noun("person", count), "by the door.")
