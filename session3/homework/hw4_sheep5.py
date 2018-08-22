sheeps = [5, 7, 300, 90, 24, 50, 75]
sheep_size = len(sheeps)

print("Hello, my name is Quinn and these are my ship sizes")
print(sheeps)
print()

for j in range(1,4):
    print("MONTH", j)
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