def binary_search(arr, target):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [0,7,2,9,36,18,125,65,79,103,30,44,3]

arr.sort()

target = int(input("Enter elemet to Search: "))

result = binary_search(arr, target)

if(result != -1):
    print("Found at index", result)
else:
    print("Not found")