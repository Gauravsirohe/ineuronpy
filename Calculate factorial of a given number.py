"""Factorial Formula
The formula to find the factorial of a number is
n! = n × (n-1) × (n-2) × (n-3) × ….× 3 × 2 × 1
"""
#5! = 5 ×4 × 3 × 2 × 1 
#5! = 1 × 2 × 3 × 4 × 5
n = int(input("Enter a number : "))
y = 1
for x in range(1,n+1):
    y = y*(x)
    print(y)
print(y)