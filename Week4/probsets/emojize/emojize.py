import emoji


prompt = input("Input: ")
output = emoji.emojize(prompt, language="alias")
print(f"Ouput: {output}")
