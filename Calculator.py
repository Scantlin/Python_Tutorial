import math
import cmath

print("This is calcualtor")
print("List of command\n" + "1. Sqaure root\n" + "2. Solve for roots")
x = int(input("Please your choice: "))

if x == 1:
    m = int(input("Enter the number: "))
    re = math.sqrt(m)
    print(re)

elif x == 2:
    def quadratic_solver(a, b, c):
    # Calculate the discriminant
        discriminant = b**2 - 4*a*c

    # Check the nature of roots
        if discriminant > 0:
            root1 = (-b + (discriminant)**0.5) / (2*a)
            root2 = (-b - (discriminant)**0.5) / (2*a)
            return root1, root2
        elif discriminant == 0:
            root = -b / (2*a)
            return root,
        else:
            root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
            root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
            return root1
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the coefficient b: "))
    c = float(input("Enter the coefficient c: "))

    roots = quadratic_solver(a, b, c)
    if len(roots) == 1:
        print(f"The root of the quadratic equation is: {roots[0]}")
    elif len(roots) == 2:
        print(f"The roots of the quadratic equation are: {roots[0]} and {roots[1]}")
    else:
        print(f"The complex roots of the quadratic equation are: {roots[0]} and {roots[1]}")


