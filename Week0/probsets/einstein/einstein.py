# Main function taking the user's mass
def main():
    mass = int(input("m: "))
    results = calculate_energy(mass)
    print(f"E: {results}")

    
# Function to calcutate Joules
def calculate_energy(m):
    # Speed of light
    c = 300000000

    # Formula to calculate joules
    joules = m * (c ** 2)
    return joules



main()

