def create_list(list1, list2):
    return list(set(list1) & set(list2))

list_a = eval(input("Enter a List: "))
list_b = eval(input("Enter another List: "))
result = create_list(list_a, list_b)
print(result)  
