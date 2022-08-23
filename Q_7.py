"""Write a python program to check whether a given number 
is positive, negative or
zero using match case statement"""

n = eval(input("Enter a number : "))
match n:
    case n if n>0:
        print("Given number is Positive")
    case n if n<0:
        print("Given number is negative")
    case n if n==0:
        print("Given number is zero")
print()