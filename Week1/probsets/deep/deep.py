def clean_up(text):
    return text.strip().lower()

question = input("What is the Answer to the Great Question of Life, the Universe, and Everythin? ")

answer = clean_up(question)

if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")


