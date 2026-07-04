happy_emoticon = ":)"
sad_emoticon = ":("

def convert(str):
    text = str.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return f"{text}"

def main():
    prompt = input("Enter a text ")
    results = convert(prompt)
    print(results)

main()
