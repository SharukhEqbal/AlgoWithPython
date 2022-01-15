# Insertion Sort
# Virtual array will be created and will keep expanding to have the sorted array
# With each operation the element will at its sorted place in sorted array
# [9,4,7,1,0,3] --> [9] [4,7,1,0,3] --> [4,9] [7,1,0,3] ...

# O (n^2)
def insertionSort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] > array[j - 1]:
                break
            else:
                array[j], array[j - 1] = array[j - 1], array[j]
    return array
    
print(insertionSort([4,6,3,10,23]))
