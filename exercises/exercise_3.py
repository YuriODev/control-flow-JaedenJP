# Your solution to Exercise 3

n = int(input("Input a number: "))
colour =""

if n == 0:
    print("Green")
elif n < 10:
    colour = "Red" if n % 2 == 1 else "Black"
elif n < 18:
    colour = "Black" if n % 2 == 1 else "Red"
elif n < 28:
    colour = "Red" if n % 2 == 1 else "Black"
elif n < 36:
    colour = "Black" if n % 2 == 1 else "Red"
else:
    colour = "The bet will not play!"

print(colour)



