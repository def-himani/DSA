# Time Complexity: O(n)
def second_max(arr):
    if not arr:
        return -1
    max = arr[0]
    prev_max = arr[0]

    for i in arr[1:]:
        if i > max:
            prev_max = max
            max = i
        elif i > prev_max:
            prev_max = i
    return prev_max

# [1,2,35,60,20,15,30] ==> 35
arr = [1,2,35,60,20,15,30]
print(second_max(arr))