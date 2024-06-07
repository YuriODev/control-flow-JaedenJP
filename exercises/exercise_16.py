# Your solution to Exercise 16

day = int(input("Input day: "))
month = int(input("Input month: "))
year = int(input("Input year: "))

if month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if day == 1:
        day = 30
        month -= 1
    else:
        day -= 1
elif month == 2 or month == 4 or month == 6 or month == 9 or month == 11:
    if day == 1:
        day = 31
        month -= 1
    else:
        day -= 1
elif month == 3:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        if day == 1:
            day = 29
            month -= 1
        else:
            day -= 1
    else:
        day -= 1
elif month == 1:
    if day == 1:
        day = 31
        month = 12
        year -= 1
    else:
        day -= 1
else:
    print("Invalid date")

print(f"{day}.{month}.{year}")