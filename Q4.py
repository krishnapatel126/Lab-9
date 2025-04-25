def sum_avg(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

marks = eval(input("Enter list of marks: "))
total, average = sum_avg(marks)
print(f"Total: {total}, Average: {average}")
