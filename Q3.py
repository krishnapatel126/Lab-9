def create_array(dim1, dim2, dim3, value):
    return [[[value for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]

array_3d = create_array(3, 4, 5, 0)
print(array_3d)
