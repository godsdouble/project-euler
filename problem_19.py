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

day = [
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
    "sunday"
]

twenty_century = [(year, leap_year(year)) for year in range(1900, 2001)]

for year in twenty_century:

    if twenty_century[year][1]:  # if it is a leap year
        month_dict["february"] = 29
    else:
        month_dict["february"] = 28



