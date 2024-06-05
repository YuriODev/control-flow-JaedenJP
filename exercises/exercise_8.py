# Your solution to Exercise 8

n = int(input("Input a 3 digit number: "))
target_number = int(input("What digit do you want to find?: "))

n1 = n // 100
n2 = (n // 10) % 10
n3 = n % 10

if n1 == target_number:
    print("True")
elif n2 == target_number:
    print("True")
elif n3 == target_number:
    print("True")
else:
    print("False")
