# Your solution to Exercise 13

n = int(input("Input 4-digit number: "))

n1 = n // 1000
n2 = (n // 100) % 10
n3 = (n // 10) % 10
n4 = n % 10

if n1 == n2 or n1 == n3 or n1 == n4 or n2 == n3 or n2 == n4 or n3 == n4:
    print("False")
else:
    print("True")