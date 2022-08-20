"""Python script to use IS operator to display if both variables are the same
object or not"""

x = input()
y = input()

result = x is y

if result == True:
    print("variables are the same object")
else:
    print("variables are not the same object")
print()
