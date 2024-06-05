# Your solution to Exercise 11

year = int(input("Input year: "))

output = "Leap year." if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else "Ordinary year."

print(output)