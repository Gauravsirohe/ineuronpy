m = int(input("Enter month in numeric format : "))
if m%400 == 0 and m%100 == 0:
    print("%d is a Leap Year" %m)
if m%4 == 0 and m%100 !=0:
    print(f"{m} is a Leap Year")
else:
    print("{0} is not a Leep Year".format(m))