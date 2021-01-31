def quick_sort(array):
    print(helper_function(array, 0, len(array) - 1))


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def helper_function(array, start_ind, end_ind):
    if start_ind >= end_ind:
        """means the array is empty"""
        return
    # selecting pivot element as first index to swap with right element easily
    # to avoid one more operation at the end to swap with first element
    pivot = start_ind

    left_index = start_ind + 1
    right_ind = end_ind
    # import pdb;pdb.set_trace()
    print(left_index, right_ind)

    # while loop will break once left index crosses right index
    while left_index <= right_ind:
        # opposite condition then swap the value
        if array[left_index] > array[pivot] > array[right_ind]:
            swap(left_index, right_ind, array)
        # if condition is then the left_index is at correct position so increment value to next
        if array[left_index] < array[pivot]:
            left_index += 1
        # if condition is then the right_index is at correct position so increment value to next
        if array[right_ind] > array[pivot]:
            right_ind -= 1

    # once left index crosses right index means value is right index is less than pivot
    # replace right index value with pivot element
    swap(pivot, right_ind, array)

    # at this point the pivot element is at its sorted position
    # now, need to sort the array to left of pivot and to the right
    # Approach should be to sort the smallest sub array first and then the largest to have less space consumption
    # calculate the smaller subarray

    length_left_array = pivot - 1 - start_ind
    length_right_array = end_ind - (pivot + 1)

    if length_left_array < length_right_array:
        # call left array first and then right as left array is smaller
        # recursive call
        # don't use pivot index to separate as pivot index is still at 0
        # take reference with right ind to which pivot value has been replaced
        helper_function(array, start_ind, right_ind - 1)
        helper_function(array, right_ind + 1, end_ind)
    else:
        helper_function(array, right_ind + 1, end_ind)
        helper_function(array, start_ind, end_ind + 1)

    return array


quick_sort([5, 6, 3, 8, 1, 10])
