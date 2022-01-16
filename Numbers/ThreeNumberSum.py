# check whether sum of three number is available in the list or not 
# [10,3,5,6,7,2,4,1], 13
# iterate in the list till len(array) - 2

def threeNumberSum(list1, targetSum):
    list1.sort()
    
    # here we have till -2 so that i value goes till third last element and we should have space for leftInd and rightInd
    leftInd = 1
    rightInd = len(list1) - 1
    for i in range(len(list1) - 2):
        if list1[i] + list1[leftInd] + list1[rightInd] == targetSum:
            return list1[i], list1[leftInd], list1[rightInd]
        elif list1[i] + list1[leftInd] + list1[rightInd] > targetSum:
            rightInd -= 1
        else:
            leftInd += 1
    return ("Target Number not found")
    
            
print(threeNumberSum([2,4,1,5,7,3], 100))
