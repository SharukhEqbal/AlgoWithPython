def isValidSubsequence1(array, sequence):
    """

    :param array:
    :param sequence:
    :return:
    """
    # Write your code here.
    count = 0
    try:
        ind = array.index(sequence[0])
    except:
        return False
    if sequence[count] in array and len(array) - 1 - ind >= len(sequence) - 1 - ind:
        count = count + 1
        for i in range(count, len(sequence)):
            for j in range(ind + 1, len(array)):
                if sequence[i] == array[j] and len(array[j:]) >= len(sequence[count:]):
                    ind = j
                    count += 1
                    break
    return count == len(sequence)


# O(n) time | O(1) space
def isValidSubsequence2(array, sequence):
    # Write your code here.

    arrIndex = 0
    seqIndex = 0

    while len(array) > arrIndex and len(sequence) > seqIndex:
        if sequence[seqIndex] == array[arrIndex]:
            seqIndex += 1
        arrIndex += 1

    return seqIndex == len(sequence)


def isValidSubsequence3(array, sequence):
    # Write your code here.
    arrIndex = 0
    seqIndex = 0

    for num in array:
        if seqIndex == len(sequence):
            break
        elif sequence[seqIndex] == num:
            seqIndex += 1

    return seqIndex == len(sequence)


print(isValidSubsequence1([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))


# print(isValidSubsequence2([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10]))


# print(isValidSubsequence()


print(isValidSubsequence1([5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 22, 6, -1, 8, 10]))
