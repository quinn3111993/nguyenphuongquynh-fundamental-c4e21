#a
n = 20
for i in range(n):
    print("*", end = " ")

#newline
print()

#b
n = int(input("Enter a number: "))
for i in range(n):
    print("*", end = " ")

#newline
print()

#c
n = 9
x = n//2
for i in range(x):
    print("x *", end = " ")
print("x", end = " ")

#newline
print()

#d
n = int(input("Enter a number: "))
x = n//2
for i in range(x):
    print("x *", end = " ")
if n % 2 != 0:
    print("x", end = " ")

#e
print()

#f
n = 7
m = 3
for i in range(m):
    for j in range(n):
        print("*", end = " ")
    print()

#g
n = int(input("Enter n: "))
m = int(input("Enter m: "))
for i in range(m):
    for j in range(n):
        print("*", end = " ")
    print()
