# Using return values rather that print functions.
# If I use print functions in this case, it will only give me a hello, there.
# It won't add the hm cuz
# A return value is data explicitly passed back to the caller of a function
# Functions simply take input and produce outputs
# In other terms, return value is simply the value the fuction gives back to us after it finishes running
def greet(input):
    if "hello" in input:
        return "hello, there"
    else:
        return "I'm not sure what you mean"

greeting = greet("how's the weather")
print("Hm,", greeting)

