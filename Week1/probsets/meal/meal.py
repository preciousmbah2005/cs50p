def main():

    time = input("What time is it? ")
    time = convert(time)

    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")
    else:
        print

def convert(time):
    # Clean the input
    time = time.lower().strip().replace(".", "").replace(" ", "")

    # Check if it's am or pm and strips the letters off
    is_pm = "pm" in time
    is_am ="am" in time
    time = time.replace("am", "").replace("pm", "")

    # Split into hours and mins
    hour, mins= time.split(":")
    hour = float(hour)
    mins = float(mins)

    # Convert 12-hour logic to 24-hour logic
    if is_pm and hour != 12:
        hour += 12
    elif not is_am and hour == 12:
        hour = 0

    # Returns the total decimal time
    return hour + (mins / 60)


if __name__ == "__main__":
    main()
