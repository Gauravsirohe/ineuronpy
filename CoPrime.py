"""Write a python script to check whether a given pair of numbers are co-Prime
numbers or not."""

n1 = int(input("Enter first number: "))
n2 = int(input("Enter Second number: "))
hcf = 1

for i in range(1, n1+1):
    if n1%i==0 and n2%i==0:
        hcf = i

if hcf == 1:
    print("Yes! They are Co-Prime.")
else:
    print("No! They are not Co-Prime.")
