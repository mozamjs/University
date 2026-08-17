my_list = [10,20,30,40,50]

def running_total(numbers):
    total = 0
    result = []

    for num in numbers:
        total += num
        result.append(total)

    return result


print("Orignal List", my_list)
print("Running Total : ", running_total(my_list))
