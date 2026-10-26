import sys
import csv

# Validate that exactly two command-line arguments were provided.
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

file_input = sys.argv[1]
file_output = sys.argv[2]

# Check that the filenames use supported image extensions.
if not file_input.endswith((".jpg", ".png")) and not file_output.endswith((".jpg", ".png")):
    sys.exit("Invalid input")

# Ensure the input and output files use the same extension.
if file_input.endswith(".jpg") and file_output.endswith(".png"):
    sys.exit("Input and output have different extensions")
elif file_input.endswith(".png") and file_output.endswith(".jpg"):
    sys.exit("Input and output have different extensions")