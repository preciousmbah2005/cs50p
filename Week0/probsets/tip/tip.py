def main():
    dollars = dollar_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * (percent / 100)
    print(f"Leave ${tip:.2f}")

def dollar_to_float(d):
    results = d.replace("$", "")
    return float(results)


def percent_to_float(p):
    results = p.replace("%", "")
    return float(results)


main()
