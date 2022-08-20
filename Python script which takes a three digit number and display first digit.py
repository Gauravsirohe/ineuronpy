"""Python script which takes a three digit number from the user and displays
only its first digit"""

number = int(input("Enter three digit number : "))

first_digit = number/100

print("First digit of %d = %d" %(number,first_digit))
