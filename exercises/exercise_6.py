# Your solution to Exercise 6

x1 = float(input("Input x1 cooridnate: "))
y1 = float(input("Input y1 cooridnate: "))
x2 = float(input("Input x2 cooridnate: "))
y2 = float(input("Input y2 cooridnate: "))

distance_a = x1**2 + y1**2
distance_b = x2**2 + y2**2

if distance_a > distance_b:
    print("A is further from the origin.")
elif distance_b > distance_a:
    print("B is further from the origin.")
else:
    print("A and B are at the same distance from the origin.")
