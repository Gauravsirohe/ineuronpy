n = int(input("Enter your choice : "))
sum = 0
for x in range(1,n+1):
    y = x+x-1
    print(y)
    sum = sum + y
print(sum)