#Calculate the area of Triangle
"""Formula to calculate Triangle
s = (a+b+c)/2
area = √(s(s-a)*(s-b)*(s-c))
where a,b,c are sides in triangle"""

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

s = (a + b + c)/2

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5


print("Area of Triangle %0.2f" %area)

