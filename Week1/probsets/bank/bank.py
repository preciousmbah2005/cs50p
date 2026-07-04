def clean_up(text):
    # .strip() removes space and .title() fixes capital letter
    return text.strip().title()

greetings = input("Greeting: ")
greet = clean_up(greetings)

if greet.startswith("Hello"):
    print("$0")
elif greet.startswith("H"):
    print("$20")
else:
    print("$100")



