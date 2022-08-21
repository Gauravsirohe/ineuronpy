a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if b<a>c:
    print(f"The greatest number is {a}")
if a<b>c:
    print(f"The greatest number is {b}")
if a<c>b:
    print(f"The greatest number is {c}")
if a is b is c:
    print("Given numbers are the same")