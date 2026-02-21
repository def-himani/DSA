# Binary Search
# Best case: O(1)
# Worst case: O(log n)

# 1. Iterative Method

def binary_search_non_recursive(arr, target):

    # Handling empty arr
    if not arr:
        return -1
    
    low = 0
    high = len(arr)

    while(high >= low):
        mid = (low + high)//2

        if(arr[mid]==target):
            return mid
        
        # value is less than middle value ---> check left
        elif(target < arr[mid]):
            high = mid - 1

        # vlaue is greater than middle value -----> check right
        else:
            low = mid + 1
    # value not in array
    return -1

# 2. Recursive Method

def binary_search_recursive(arr, target, low = 0, high = None):
    if not arr:
        return -1

    if high is None:
        high = len(arr)-1

    if(high < low):
        return -1
    
    mid = (low + high) // 2
    if(arr[mid] == target):
        return mid
    elif(target < arr[mid]):
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)


# Output
# arr = [1,6,7,9,10,13,15,20]
# print(binary_search_recursive(arr, 20))
# print(binary_search_non_recursive(arr, 20))