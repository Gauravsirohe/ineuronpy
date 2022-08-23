"""Write a python program to check whether 
a given string is a multiword string or 
single word string using match case statement"""

st = input("Enter a word")
x = len(st)
match x:
    case 1:
        print("Single Word String")
    case x if x>1:
        print("Multiword String")
    case x if x==False: #condition when we did not provide any word, just a case of zero string
        print("No string has been entered")
print()