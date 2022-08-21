m = int(input("Enter month in numeric format :"))
if m ==1:
    print("January", "No of days : 31", sep="<")
elif m ==2:
    print("Feburary", "No of days : 28", sep="<")
elif m ==3:
    print("March", "No of days : 31", sep="<")
elif m ==4:
    print("April", "No of days : 30", sep="<")
elif m ==5:
    print("May", "No of days : 31", sep="<")
elif m ==6:
    print("June", "No of days : 30", sep="<")
elif m ==7:
    print("July", "No of days : 31", sep="<")
elif m ==8:
    print("August", "No of days : 31", sep="<")
elif m ==9:
    print("September", "No of days : 30", sep="<")
elif m ==10:
    print("October", "No of days : 31", sep="<")
elif m ==11:
    print("November", "No of days : 30", sep="<")
elif m ==12:
    print("December", "No of days : 31", sep="<")
else:
    print()

#Advance method
m = [1,3,5,7,8,10,12]
mm = [4,6,9,11]
mmm = [2]
n = int(input("Enter month in numeric : "))
y = int(input("Enter year : "))
if n in m:
    print("31")
elif n in mm:
    print("30")
elif n in mmm:
    if y%4 ==0:
        print("29")
    else:
        print("28")
else:
    print("Enter correct month value")
