#Asks users enter a number and then calculates factorial of n
n = int(input("Enter a number: "))
factorial = 1
for i in range(1,n+1):
    factorial *= i
print(str(n) + "! =", factorial)
