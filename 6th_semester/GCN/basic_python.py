# # Exercise 1: Create a list of integers from 1 to 5 and print it.
# arr = [1, 2, 3, 4, 5]
# print(arr)

# print(arr[2]) #for printing the single item of array

# arr[2] = 99 #updating the value of array at index 2
# print(arr)

# arr.append(49)

# arr.remove(5)#removes the first occurrence of 5 in the list

# print(arr)
# arr.pop(1) #removes the item at index 1

# print(arr)
# print(len(arr))


# # Exercise 2: Traversing array 

# arr = [12,7,19,4,25]
# # by value
# for x in arr:
#     print(x)
# # by index
# for i in range(len(arr)):
#     print(i, arr[i])
# # index + value both using enumerate() 
# for i,x in enumerate(arr):
#     print(i, x)


# 3-array.array
# import array 

# val = array.array('i',[1,2,3,4,5,6,7,8])

# for i in range(0,6):
#     print(val[i],end= " ")

# print('\n')

# for i in range(0,len(val)):
#     print(val[i], end = " ")

# print('\n')

# for x in val:
#     print(x, end = " , ")

# print('\n')

# val.reverse()

# for i in range(0,len(val)):
#     print(val[i], end = " ")


# insert Element 

from array import *
val = array('i',[1,2,3,4,5,6,7,8])

