a = int(input("Enter a digit for real: "))
b = int(input("Enter a digit for imag : "))
c = complex(a,b)
if c.real > c.imag:
    print("Real part is greatest",c.real)
elif c.real < c.imag:
    print("Imaginary part is greatest",c.imag)
else:
    print(f"Real and Imaginary having same value as {c.real}")
