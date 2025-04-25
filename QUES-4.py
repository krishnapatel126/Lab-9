def reverse_list(lst):
    if len(lst) == 0:
        return []
    return [lst[-1]] + reverse_list(lst[:-1])

input_list = list(map(int, input("Enter numbers separated by space: ").split()))
reversed_list = reverse_list(input_list)
print(f"Reversed list: {reversed_list}")
