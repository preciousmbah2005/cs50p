# hello.py
# My first Python program
# Week 0 - Functions and Variables

# Ask user for their name
name = input("What's your name? ")

# Remove extra spaces and capitalize correctly
name = " ".join(name.split()).title()

# Say hello to the user
print(f"Hello, {name}")

"""
Older version

name = input("What's your name? ")
print("Hello,", name)
"""

"""
Another version

name = input("What's your name? ")
print(f"Hello, {name}")
"""
