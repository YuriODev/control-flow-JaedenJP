# Your solution to Exercise 15

day = int(input("Input day: "))
month = int(input("Input month: "))
year = int(input("Input year: "))

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
    if day == 31:
        day = 1
        month += 1
    else:
        day += 1
elif month == 4 or month == 6 or month == 9 or month == 11:
    if day == 30:
        day = 1
        month += 1
    else:
        day += 1
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        if day == 29:
            day = 1
            month += 1
        else:
            day += 1
    else:
        if day == 28:
            day = 1
            month += 1
        else:
            day += 1
elif month == 12:
    if day == 31:
        day, month = 1, 1
        year += 1
    else:
        day += 1
else:
    print("Invalid date")

print(f"{day}.{month}.{year}")