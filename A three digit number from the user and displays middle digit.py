"""Python script which takes a three digit number from the user and displays
only its middle digit"""

number = int(input("Enter a three digit number : "))

remove_last_digit = number%100 #remove first digit

mid_digit = remove_last_digit/10 #after remove first digit , we get first number from remaining two digit which is midle digit of 3 digit number

print("%d" %mid_digit)
