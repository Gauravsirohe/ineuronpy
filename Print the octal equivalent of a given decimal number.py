N = int(input("Enter a number : "))
binarystring = ""
while N:
    reminder = N%8 # remider
    N = N//8  #division
    reminder = str(reminder)
    binarystring = binarystring+reminder
print(binarystring[::-1], end="")
