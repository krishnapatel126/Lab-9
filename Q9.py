def count_alpha_digits(s):
    alpha_count = sum(1 for char in s if char.isalpha())
    digit_count = sum(1 for char in s if char.isdigit())
    return {'alphabets': alpha_count, 'digits': digit_count}

input_string = input("Enter a string: ")
result = count_alpha_digits(input_string)
print(result)
