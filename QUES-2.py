def to_binary(n):
    if n == 0:
        return ""
    else:
        return to_binary(n // 2) + str(n % 2)

number = int(input("Enter a positive integer: "))
binary_representation = to_binary(number)
print(f"Binary equivalent of {number} is: {binary_representation}")
