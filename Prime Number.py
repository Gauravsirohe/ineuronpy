#Python script to check whether a given number is Prime or not
"""Prime numbers: a whole number greater than 1 that cannot be 
exactly divided by any whole number other than itself and 1 """

n = int(input("Enter a number : "))
for i in range(2,n):
    if n%i == 0:
        print("Not a Prime Number")
        break
else:
    print("Prime Number")

    
