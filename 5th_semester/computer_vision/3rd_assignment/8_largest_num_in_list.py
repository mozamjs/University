
number = [34,7,89,23,55,12,99,41]

# largest = max(number)

largest = number[0]

for num in number:
    if num > largest:
        largest = num

print("List:", number)
print("Largest element is :" , largest)



