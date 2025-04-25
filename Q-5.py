names = input("Enter names of faculty members separated by commas: ").split(',')
long_names = list(filter(lambda name: len(name.strip()) > 8, names))
print("Names longer than 8 characters:", long_names)
