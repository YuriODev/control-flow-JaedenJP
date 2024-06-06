# Your solution to Exercise 5

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

d = b**2 - (4*a*c)

x1 = 0
x2 = 0

output = ""

if a == 0 and b == 0 and c == 0:
    output = "Infinite roots."
elif a == 0 and b == 0 and c != 0:
    output = "No roots."
elif a == 0:
    if b != 0:
        output = -c/b
elif b == 0:
    if a != 0:
        output = (-c/a)**0.5
elif c == 0:
    if a != 0:
        output = "No roots."
    elif b != 0:
        output = -b/a
elif d < 0:
    output = "No roots."
elif d == 0:
    output = -b/(2*a)
elif d > 0:
    x1 = (-b + (d**0.5))/(2*a)
    x2 = (-b - (d**0.5))/(2*a)
    output = f"{x1} and {x2}"
else:
    output = "No roots."

print(output)
        