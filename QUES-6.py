def sanitize_list(lst):
    if not lst:
        return []
    return [max(0, lst[0])] + sanitize_list(lst[1:])

input_list = list(map(int, input("Enter numbers separated by space: ").split()))
sanitized_list = sanitize_list(input_list)
print(f"Sanitized list: {sanitized_list}")
