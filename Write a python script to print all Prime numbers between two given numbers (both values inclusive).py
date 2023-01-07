"""Write a python script to print all Prime numbers between two given numbers (both
values inclusive)"""

frst = int(input("Enter first digit: "))
lst = f = int(input("Enter first digit: "))

for p in range(frst,lst+1):
    for i in range(2,p):
        if p%i == 0:
            break
    else:
        print(p)