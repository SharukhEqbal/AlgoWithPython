# second maximum without sorting
# [10, 2, 5, 1, 19]
# find the max of first 2 element in list and assign it to maxInList variable
# assign the secondmaxInList with min in first 2 element in list

def secondLargestNumber(array):
    maxInList = max(array[0], array[1])
    secondmaxInList = min(array[0], array[1])

    for i in range(2, len(array)):
        if array[i] > maxInList:
            secondmaxInList = maxInList
            maxInList = array[i]
        elif array[i] > secondmaxInList and array[i] != maxInList:
            secondmaxInList = i
    print(secondmaxInList)
    
#secondLargestNumber([10, 2, 5, 1, 19])

def secondLargestNumber(array):
    maxInList = array[0]
    secondmaxInList = array[0]
    
    for i in array:
        if i > maxInList:
            maxInList = i
        if i > secondmaxInList and i != maxInList:
            secondmaxInList = i
    return maxInList, secondmaxInList

print(secondLargestNumber([10, 2, 5, 1, 19]))
