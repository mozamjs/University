my_list = [1,55,113,6,296,19,21,369,15,55,500,60,80,7,98,108,79]

search = int(input("Enter a number to search : "))

found = False

for num in my_list:
    if num == search:
        found = True
        index = my_list.index(num)
        break

print("List:", my_list)

if found:
    print(search , "is exists in list at index: ",index)
else:
    print(search, "is not present in the list")