#Write a python script to print first N terms of a Fibonacci series
"""f = 0 1 1 2 3 5 8"""

N = int(input("Enter a number to print Fibonacci Series: "))

frst = 0
lst = 1

while N:
    print(frst)
    nth = frst + lst
    frst = lst
    lst = nth
    N = N-1
    