"""Cuboid is a solid box whose every surface is a rectangle of same area or different areas.
A cuboid will have a length, breadth and height.

Volume of a cuboid = Length × Width × Height cubic units."""

l = float(input("Enter length (cm) : "))
w = float(input("Enter width (cm) : "))
h = float(input("Enter height (cm) : "))

v = l*w*h

print("The volume of a cuboid:", v,"cm")
