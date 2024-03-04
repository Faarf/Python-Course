months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    try:
        m,d,y = date.split("/")
        m = int(m)
        d = int(d)
        y = int(y)
        if m < 13 and d < 32:
            print (y, f"{m:02}", f"{d:02}", sep="-")
            break
    except:

        try:
            if "," in date:
                m, d, y = date.split(" ")
                d = d.replace(",","")
                d = int(d)
                y = int(y)
                if m in months and d < 32:
                    m = months.index(m)+1
                    print(y, f"{m:02}",f"{d:02}", sep="-")
                    break
            else:
                pass

        except (ValueError, IndexError):
            pass
