def average(lst):
    if not lst:
        return 0
    return (lst[0] + average(lst[1:])) / len(lst)

input_list = list(map(int, input("Enter numbers separated by space: ").split()))
if input_list:
    avg = average(input_list)
    print(f"Average of the list: {avg}")
else:
    print("The list is empty.")
