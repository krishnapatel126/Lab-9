def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

a = int(input("Enter base (a): "))
b = int(input("Enter exponent (b): "))
result = power(a, b)
print(f"{a} raised to the power of {b} is: {result}")
