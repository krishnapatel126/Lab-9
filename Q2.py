def compute(n):
    n_str = str(n)
    result = n + int(n_str * 2) + int(n_str * 3) + int(n_str * 4)
    return result

for i in range(4, 8):
    print(f"compute({i}) = {compute(i)}")
