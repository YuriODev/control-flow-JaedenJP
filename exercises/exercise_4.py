# Your solution to Exercise 4

grade = int(input("Input grade: "))

if 1 <= grade <= 3:
    print("initial level")
elif 4 <= grade <= 6:
    print("average level")
elif 7 <= grade <= 9:
    print("sufficient level")
elif 10 <= grade <= 12:
    print("high level")
else:
    print("level is absent")