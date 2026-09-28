months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12

}

while True:
    try:
        user_input = input("Date: ")
        if "/" in user_input:
            Month, Day, Year = user_input.split("/")
            Month = int(Month)
            Day = int(Day)
            Year = int(Year)
        else:
            Month, Day, Year = user_input.split()
            Month = months[Month]
            Year = int(Year)
            if "," not in Day:
                continue
            Day = Day.replace(",", "")
            Day = int(Day)

        if not (1 <= Month <= 12 and 1 <= Day <= 31):
            continue

        print(f"{Year}-{Month:02}-{Day:02}")
        break

    except(ValueError, KeyError):
        continue

