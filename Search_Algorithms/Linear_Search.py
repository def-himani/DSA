def linear_search(arr, target):
    for i in range(len(arr)):
        if(arr[i] == target):
            return i
    return -1

# Implementation / Verification
# arr = [4,6,9,1,7,3]

# result = linear_search(arr, 3)

# if (result != -1):
#     print("Index of the target is: ", result)
# else:
#     print("Target not found in Array")