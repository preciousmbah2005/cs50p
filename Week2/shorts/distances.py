distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "New Horizons": 58,
    "Pioneer 11": 44
}

def main():

    #This is to access the values in the dictionary and loop over with aa loop
    for distance in distances.values():
        print(f"{distance} is {convert(distance)} m")

    # This is to access the keys in the dictionary and loop over with a for loop
    """
    for name in distances.keys():
        print(f"{name} is {distances[name]} AU from Earth")

    """

def convert(au):
    return au * 149597870700

main()
