import re

email = input("What's your email? ").strip()

if re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
    print("Valid")
else:
    print("Invalid")