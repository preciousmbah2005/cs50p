import re

email = input("What's your email? ").strip()

if re.search(r".+@.+\.com", email):
    print("Valid")
else:
    print("Invalid")