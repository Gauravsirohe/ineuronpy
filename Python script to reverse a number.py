#n = input("Enter a Number : ")
#print(n [::-1])
num = int(input("Please provide the number to be reversed: "))
reversed_number = 0
while num>0:
    reminder = num%10
    num= num//10
    print(reminder, end="")

