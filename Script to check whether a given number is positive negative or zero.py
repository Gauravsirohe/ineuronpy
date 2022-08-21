# positive no = 1,2,3...
#non positive no = 0,-1,-2,-3...
#negative = -1,-2,-3....

n = int(input("Enter a number: "))
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
elif n == 0:
    print("Zero")
else:
    print()