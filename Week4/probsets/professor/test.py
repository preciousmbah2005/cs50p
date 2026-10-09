import random

# Generate two random numbers
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
correct_answer = num1 + num2

# Ask the user for the answer
user_input = int(input(f"What is {num1} + {num2}? "))

# Check if the answer is wrong
while user_input != correct_answer:
  print("That is wrong. Try again!")
  # Re-ask using the exact same num1 and num2
  user_input = int(input(f"What is {num1} + {num2}? "))

print("Correct!")