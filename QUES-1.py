def prime_factors(n, divisor=2):
    if n < 2:
        return []
    if n == 1:
        return []
    if n % divisor == 0:
        return [divisor] + prime_factors(n // divisor, divisor)
    else:
        return prime_factors(n, divisor + 1)

number = int(input("Enter a positive integer: "))
factors = prime_factors(number)
print(f"Prime factors of {number} are: {factors}")
