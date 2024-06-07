# Your solution to Exercise 17

ticket = str(input("Input ticket number: "))

n1 = int(ticket) // 100000
n2 = (int(ticket) // 10000) % 10
n3 = (int(ticket) // 1000) % 10
n4 = (int(ticket) // 100) % 10
n5 = (int(ticket) // 10) % 10
n6 = int(ticket) % 10

if n1 + n2 + n3 == n4 + n5 + n6:
    print("Happy")
else:
    print("Ordinary")
