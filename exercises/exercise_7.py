# Your solution to Exercise 7

no1 = float(input("Input number: "))
no2 = float(input("Input number: "))
operation = input("What operation?: ")

if operation == "+":
    print(no1 + no2)
elif operation == "-":
    print(no1 - no2)
elif operation == "*":
    print(no1 * no2)
elif operation == "/":
    if no2 == 0:
        print("Division by 0!")
    else:
        print(no1 / no2)
elif operation == "mod":
    print(no1 % no2)
elif operation == "pow":
    print(no1 ** no2)
elif operation == "div":
    if no2 == 0:
        print("Division by 0!")
    else:
        print(no1 // no2)
else:
    print("Operation not supported!")
