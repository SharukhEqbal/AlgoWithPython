# Bubble Sort 
# With each iteration the largest element moves to rightmost
# need to use 2 loop first loop runs n times and second list limited to n - i 
# if list becomes sorted inbetween exit the loop 
# the first loop should be while so that if the second loop doesn't do any swapping then the sorted value remains True


def bubbleSorterHelper(list1):
    isSorted = False
    while not isSorted:
        isSorted = True
        for j in range(len(list1) - 1 ):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
                isSorted = False
    return list1

print(bubbleSorterHelper([2, 14, 3, 25, 10]))      
