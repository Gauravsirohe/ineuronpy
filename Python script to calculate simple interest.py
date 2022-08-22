"""Simple Interest Formula A = P(1 + rt)
where P = Principle
r = rate of Interest
t = period of time in years"""

t = int(input("Time Period in years: "))
r = int(input("Rate of Interest per year: "))
P = float(input("Principal Amount: "))

A = P*(1 + (r/100)*t)

print("Simple Interest:", A)
