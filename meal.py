# Input a time in ##:## or #:## to see if its breakfast, lunch, or dinner time.

def main():
    time = input("What time is it? ")
    meal = convert(time)

    if meal >= 7 and meal <= 8:
        print("breakfast time")

    elif meal >= 12 and meal <= 13:
        print("lunch time")

    elif meal >= 18 and meal <= 19:
        print("dinner time")

# Optional challenge, to add "a.m" and "p.m" support.

def convert(time):
    hours, minutes = time.split(":")
    if "p.m" in minutes:
        new_hours = float(hours) + 12
        new_minutes = minutes.removesuffix("p.m")
        real_minutes = float(new_minutes) / 60
        return float(new_hours) + float(real_minutes)

    elif "a.m" in minutes:
        new_minutes = minutes.removesuffix("a.m")
        real_minutes = float(new_minutes) / 60
        return float(hours) + float(real_minutes)

    else:
        new_minutes = float(minutes) / 60
        return float(hours) + float(new_minutes)

# vv This is for CS50's debugging vv
if __name__ == "__main__":
    main()



