def three_top_max(arr):
    if not arr:
        return -1
    
    first = float('-inf')
    second= float('-inf')
    third = float('-inf')

    for i in arr:
        if i > first:
            third = second
            second = first
            first = i
        elif i < first and i > third:
            third = second
            second = i
        elif i > third and i < second and i < first:
            third = i

    res = []
    if first == float('-inf'):
        return res
    res.append(first)
    if second == float('-inf'):
        return res
    res.append(second)
    if third == float('-inf'):
        return res
    res.append(third)
    
    return res

arr1 = [1,3,4,4,5,6,8,9,11,40,22,40,40,1,187,187,3,45,3,4,40]
arr2 = [1,3]
arr3 = [187,187,3,45,3,0]
res = three_top_max(arr3)
print(" ".join(map(str, res)))