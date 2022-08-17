import datetime #datetime is a module
dt = datetime.datetime.now() #datetime is a class and now(), today() is method, so using datetime.now()
#print (dt.strftime("%d-%m-%Y and %H:%M:%S"))
print (dt.strftime("%d-%m-%Y and %I:%M %p")) #strftime is used to format datetime in string format

