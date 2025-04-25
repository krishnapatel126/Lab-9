def ispalindrome(s):
    cleaned = ''.join(s.split()).lower()
    return cleaned == cleaned[::-1]

test_string = input("Enter a string: ")
print(ispalindrome(test_string))  
