def leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False


month_dict = {
    "january": 31,
    "february": 28,
    "march": 31,
    "april": 30,
    "may": 31,
    "june": 30,
    "july": 31,
    "august": 31,
    "september": 30,
    "october": 31,
    "november": 30,
    "december": 31
}

day = (
    None,
    ("monday", 1),
    ("tuesday", 2),
    ("wednesday", 3),
    ("thursday", 4),
    ("friday", 5),
    ("saturday", 6),
    ("sunday", 7)
)

twenty_century = [(year, leap_year(year)) for year in range(1900, 2001)]
first_of_month = day[1]
tracker = []

for year in twenty_century:

    if year[1]:  # if it is a leap year
        month_dict["february"] = 29
    else:
        month_dict["february"] = 28

    for month in month_dict:
        if first_of_month == day[7]:
            tracker.append((year, month))
        r = (month_dict[month] + 1) % 7
        if r != 0:
            index = 7 - r + first_of_month[1]
            if index > 7:
                index -= 7
            first_of_month = day[index]

print(tracker)
print(len(tracker))
