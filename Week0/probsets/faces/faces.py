happy_emoticon = ":)"
sad_emoticon = ":("

def main():
    prompt = input("Enter a text: ")
    results = convert(prompt)
    print(results)

def convert(str):
    text = str.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return f"{text}"


main()
