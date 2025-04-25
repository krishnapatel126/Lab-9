lst = input("Enter list elements (strings/numbers) separated by commas: ").split(',')
palindromes = [x for x in lst if str(x) == str(x)[::-1]]
print("Palindromic entries in the list:", palindromes)
