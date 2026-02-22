# Problem:

# Numbers in an array will keep increasing until one point. After that it will decrease. Find the maximum in such an array.
# Input:
# [1, 2, 4, 5, 7, 8, 3]
# [10, 20, 30, 40, 50]
# [120, 100, 80, 20, 0]

def bitonic_max(arr):

    if not arr:
        return -1
    n = len(arr)
    if n == 1 or arr[0] > arr[1]:
        return arr[0]

    if arr[n-1] > arr[n-2]:
        return arr[n-1]
    
    low = 1
    high = n - 1


    while(high >= low):
        mid = (low + high) // 2
        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return arr[mid]
        elif arr[mid] > arr[mid-1]: # go right [10 > 9]
            low = mid + 1
        else: # go left
            high = mid - 1

# arr1 = [1,2,3,4,5,6,8,9,15,190,19,15,6,2,0]
# arr2 = [290,19,15,6,2,0]
# arr3 = [1,2,3,4,5,6,8,9,15,390]
# print(bitonic_max(arr1))
# print(bitonic_max(arr2))
# print(bitonic_max(arr3))