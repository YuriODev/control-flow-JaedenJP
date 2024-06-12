# Your solution to Exercise 9

n = int(input("Input a 3 digit number: "))

n1 = n // 100
n2 = (n // 10) % 10
n3 = n % 10

total = n1 + n3

if total > n2:
    print(">")
elif total < n2:
    print("<")
else:
    print("=")