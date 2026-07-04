# A side effect is anything that gets change while our function is still running
# Like changing a variable inside of a function
emoticon = "v.v"

def main():
    global emoticon
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh, hi!")

def say(phrase):
    print(phrase , emoticon)

main()

