"""Three digit number from the user and displays
only its last digit."""

n = int(input("Enter a three digit number : "))

lstd = n%10

print("Last digit of number %d = %d" %(n,lstd))
