"""Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number."""

n = int(input("Enter a number: "))
match n:
    case n if n%2==0 and n>0:
        print("Saurabh Shukla")
    case n if n%2!=0 and n<0:
        print("Prateek Jain")
    case n if n%2!=0 and n>0:
        print("Aditya Choudhary")
    case _:
        print("0 is constant")
print()