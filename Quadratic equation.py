"""The roots of the quadratic equation ax2 + bx + c = 0, a ≠ 0 are given by the following formula:
quadratic equation
In this formula, the term b2 - 4ac is called the discriminant.
If b2 - 4ac = 0, then the equation has two equal roots.
If b2 - 4ac > 0, the equation has two real roots.
If b2 - 4ac < 0, the equation has two complex roots."""

a = int(input("Enter values of a: "))
b = int(input("Enter values of b: "))
c = int(input("Enter values of c: "))
# b square - 4ac
d = b**2 - 4*a*c
if d == 0:
    print("Equation has two equal roots")
elif d > 0:
    print("Equation has two roots")
else:
    print("Equation has two complex roots")
