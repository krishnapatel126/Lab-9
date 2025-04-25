def count_vowels(s):
    if not s:
        return 0
    vowels = 'aeiouAEIOU'
    return (1 if s[0] in vowels else 0) + count_vowels(s[1:])

input_string = input("Enter a string: ")
vowel_count = count_vowels(input_string)
print(f"Number of vowels in the string: {vowel_count}")
