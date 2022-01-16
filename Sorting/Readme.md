#Quick sort
# create a pivot element as first element left pointer 1st element right pointer last element
# compare pivot element with left if pivot > left pointer and pivot < right pointer replace left and right pointer
# if pivot < left pointer increment left pointer 
# if pivot > right pointer decrease the right pointer
# if left > right pointer replace pivot with right pointer
# with each iteration pivot will be at right position
# O(nlogn)

# Bubble sort
# compare the next value if it is greater swap 
# with each iteration the max value will at the end
# two loops will be used O(n^2) one will iterate and another will be with isSorted while loop
# Have a variable as isSorted = False and make it as true means if no swapping done in complete iteration the list is sorted
# run the loop till n - i so that element which are already sorted can be skipped

# Insertion Sort
# Create a virtual array at start with first index value
# use two loop first loop starts from 1 second loop starts from j = i
# compare j and j - 1 value if j - 1 is bigger swap the value
# decrement j value till 1 and compare
# with this the virtual sorted array will keep on increasing

# i = 1 [2,5],[6,3,7,1]
# i = 2 5>6 F[2,5,6], [3,7,1]
# i = 3 6>3T [2,5,3,6] 5>3T [2,3,5,6] 2>3F [2,3,5,6] [7,1]

# Selection Sort
# select the number and compare it with 1, i=0 j = i + 1 len(array) element with each iteration find the smallest number and place it from left
# O(n^2)

#Merge Sort

