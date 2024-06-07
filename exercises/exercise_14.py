# Your solution to Exercise 14

n = int(input("Input 4-digit number: "))

n1 = n // 1000
n2 = (n // 100) % 10
n3 = (n // 10) % 10
n4 = n % 10

if n1 == n4 and n2 == n3:
    print("True")
else:
    print("False")