n = int(input("Enter a number : "))
sum = 0
for x in range(1, n+1):
    sum = sum + x**2
print(sum, end = " ")