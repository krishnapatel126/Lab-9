def create_tuples_list(n):
    return [(x, x**2, x**3) for x in range(1, n + 1)]

tuples_list = create_tuples_list(5)
print(tuples_list)
