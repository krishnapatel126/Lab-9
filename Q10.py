def frequency(s):
    words = s.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return dict(sorted(freq.items()))

input_string = input("Enter a string: ")
result = frequency(input_string)
print(result)
