a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a != 0:
    delta = b**2 - 4*a*c
    delta_sqrt = delta**0.5
    a_2 = a*2
    if delta > 0:
        x_1 = (-b - delta_sqrt)/a_2
        x_2 = (-b + delta_sqrt)/a_2
        print("Your equation has 2 roots: x_1 =", x_1, "and x_2 =", x_2)
    elif delta == 0:
        x = -b/(a_2)
        print("Your equation has 1 root only: x =", x)
    else:
        print("Your equation has no root!")
elif b != 0:
    x = -c/b
    print("This is not a quadratic equation. It has 1 root only: x=", x)
else:
    print("This is not a quadratic equation. Your equation has no root!")

