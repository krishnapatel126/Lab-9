list1 = list(map(int, input("Enter 6 numbers for list1 separated by space: ").split()))
list2 = list(map(int, input("Enter 6 numbers for list2 separated by space: ").split()))
result = list(map(lambda x, y: x + y, list1, list2))
print("Resulting list after adding corresponding elements:", result)
