num = int(input("How many prime number wants to print? "))

for p in range(2,(num*3)-2):
    for i in range(2,p):
        if p%i == 0:
            break
    else:
        print(p, end =" ")


            
            
