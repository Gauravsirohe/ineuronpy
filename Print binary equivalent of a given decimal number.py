n = int(input("Enter a number - "))
print(bin(n)[2:]) #Using bin function
binastring=""
while n > 0: #Using loop
    reminder = n%2
    n = n//2
    reminder = str(reminder)
    binastring = binastring+reminder
print(binastring[::-1], end ="")
