# Your solution to Exercise 12

n = int(input("Input 4 digit number: "))

n1 = n // 1000
n2 = (n // 100) % 10
n3 = (n // 10) % 10
n4 = n % 10

n1 = "*" if n1 % 2 == 0 else str(n1)
n2 = "*" if n2 % 2 == 0 else str(n2)
n3 = "*" if n3 % 2 == 0 else str(n3)
n4 = "*" if n4 % 2 == 0 else str(n4)

print(n1 + n2 + n3 + n4)