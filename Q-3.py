import random

numbers = [int(input(f"Enter number {i+1} between -15 and 15: ")) for i in range(10)]
squares = list(map(lambda x: x**2, numbers))
print("Original numbers:", numbers)
print("Squares of the numbers:", squares)
