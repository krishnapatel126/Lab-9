def count_lower_upper(s):
    lower_count = sum(1 for char in s if char.islower())
    upper_count = sum(1 for char in s if char.isupper())
    return {'lowercase': lower_count, 'uppercase': upper_count}
            
sample_string = input("Enter the string: ")
result = count_lower_upper(sample_string)
print(result)  
