sheeps = [5, 7, 300, 90, 24, 50, 75]
sheep_size = len(sheeps)

print("Hello, my name is Quinn and these are my ship sizes")
print(sheeps)
print()

max_sheep = max(sheeps)
print("Now my biggest sheep has size", max_sheep, "let's shear it")
sheeps[sheeps.index(max_sheep)] = 8
print("After shearing, here is my flock")
print(sheeps)
print()

for j in range(1,3):
    print("MONTH", j, ":")
    for i in range(sheep_size):
        sheeps[i] += 50
    print("One month has passed, now here is my flock")
    print(sheeps)
    max_sheep = max(sheeps)
    print("Now my biggest sheep has size", max_sheep, "let's shear it")
    sheeps[sheeps.index(max_sheep)] = 8
    print("After shearing, here is my flock")
    print(sheeps)
    print()
print("MONTH 3 :")
for i in range(sheep_size):
    sheeps[i] += 50
print("One month has passed, now here is my flock")
print(sheeps)
print()

total_size = 0
for i in sheeps:
    total_size += i
price = 2
print("My flock has size in total:", total_size)
print("I would get ", total_size, " * ", price, "$ = ", total_size*price, "$", sep="")