def ispangram(s):
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet_set <= set(s.lower())

test_string = input("Enter a string: ")
print(ispangram(test_string))
