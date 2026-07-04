text = input("Input: ")

output = ""
for character in text:
    if character not in "aeiouAEIOU":
        output += character

print(f"Output: {output}")
