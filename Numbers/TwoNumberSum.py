# check whether sum of two number is available in the list or not 
# [10,3,5,6,7,2,4,1], 13
# [1,2,3,4,5,6,7,10]
# sort the numbers and use pointer to add numbers from left and right
# number is greater move right to left else move left to right

def twoNumberSum(list1, targetSum):
    list1.sort()
    l = 0
    r = len(list1) - 1
    
    while l < r:
        if list1[l] + list1[r] == targetSum:
            return (list1[l], list1[r], targetSum)
        elif list1[l] + list1[r] > targetSum:
            r -= 1
        elif list1[l] + list1[r] < targetSum:
            l += 1
    return ("Target Sum is not found")
    
print(sumOfTwoNumber([10,3,5,6,7,2,4,1], 100))
