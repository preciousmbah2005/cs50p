# Defining the main function that replaces each space with "..."
def main():
    
    text = get_users_input("Enter a sentence ")
    print(text_replace(text))

# Get user's input
def get_users_input(prompt):
    users_input = input(prompt)
    return users_input

# Defining the function that replaces the space with "..."
def text_replace(text):
    return text.replace(" ", "...")

main()
