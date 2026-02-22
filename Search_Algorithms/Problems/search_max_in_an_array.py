# Given an array, find the max element
# Worst case time complexity: O(n)

# Iterative
def find_max(arr):
    if not arr:
        return -1
    
    max = arr[0]

    for i in arr[1:]:
        if(i>max):
            max = i
    return max

# Recursive
def find_max_recursive(arr, n= None):
    if not arr:
        return -1
    if n == None:
        n = len(arr)
    if n == 1:
        return arr[0]
    
    prev = find_max_recursive(arr, n-1)

    return max(prev, arr[n-1])

# Example
# arr = [-2000,4222.43,6,0,1,8]
# arrd = []

# print(find_max(arr))
# print(find_max_recursive(arrd))