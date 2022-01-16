# BinarySearch only works for sorted array
# assign left pointer to first element and right pointer to rightmost element
# calculate the mid element and compare the searching element
# if value is greater than mid then update the left pointer with 1 else update the right pointer by mid + 1

def binarySearch(array, ele):
    l = 0
    r = len(array) - 1
    return binaryHelper(array, l, r, ele)

def binaryHelper(array, l, r, ele):
    mid = (l + r) // 2
    
    while l < r:
        if array[mid] == ele:
            return mid, ele
        elif array[mid] > ele:
            l = mid + 1
            binaryHelper(array, l, r, ele)
        else:
            r = mid - 1
            binaryHelper(array, l, r, ele)
    
    return "Element Not found"

print(binarySearch([1,5,16,27,33,103], 13))
