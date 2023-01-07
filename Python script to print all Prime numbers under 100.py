for Number in range(1,100):
    if Number>1:
        for i in range(2,Number):
            if (Number%i)==0:
                break
        else:
            print(Number)
