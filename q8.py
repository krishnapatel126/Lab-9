def convert(s):
    words = s.split()
    unique_sorted_words = sorted(set(words))
    return ' '.join(unique_sorted_words)

input_string = input("Enter a string: ")
result = convert(input_string)
print(result)
