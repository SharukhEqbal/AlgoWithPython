# O(N) time complexity and O(1) space complexity
def palindromeStringCheck(given_string):
    """
    :param given_string:
    :return: True if number is palindrome and False if number is not a palindrome
    """
    left_index = 0
    right_index = len(given_string) - 1

    while left_index < right_index:
        if given_string[left_index] == given_string[right_index]:
            left_index += 1
            right_index -= 1
        else:
            return False
    return True


# O(N) time complexity O(N) space complexity
def palindromeNumberCheck2(given_number):
    temp_number = given_number
    reverse_number = 0

    while given_number > 0:
        divisor = given_number % 10
        reverse_number = reverse_number*10 + divisor
        given_number = given_number // 10

    if temp_number == reverse_number:
        return True
    else:
        return False


# O(N) space and time complexity # O(N) space because of call stack memory storage in recursion
def palindromeCheckRecursion(given_string, index=0):
    reverse_index = len(given_string) - 1 - index
    if index >= reverse_index:
        return
    else:
        return given_string[index] == given_string[reverse_index] and palindromeCheckRecursion(given_string, index+1)

