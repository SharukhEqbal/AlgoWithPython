import copy

# Sum of two number in an array

# O(n^2) time | O(1) space
def twoNumberSum1(arr, sum):
    for i in range(len(arr) - 1):
        for j in range(i, len(arr)):
            if arr[i] + arr[j] == sum:
                return arr[i], arr[j]
    return []

# [3, 5, -4, 8, 11, 1, -1, 6] targetSum: 10
# [14] targetSum: 15
# [4, 6] targetSum: 10
def twoNumberSum2(arr, sum):
    for i in range(1, len(arr)):
        if arr[0] + arr[i] == sum:
            return arr[0], arr[i]
    arr.pop(0)
    if len(arr) >= 2:
        twoNumberSum2(arr, sum)
    return []

# O(n) time | O(n) space
def twoNumberSum3(arr, sum):
    nums = {}
    for num in arr:
        mat = sum - num
        if mat in nums:
            return [mat, num]
        else:
            nums[num] = True
    return []


# [3, 5, -4, 8, 11, 1, -1, 6] targetSum: 10
# sort [-4, -1, 1, 3, 5, 6, 8, 11]
# O(nlog(n)) | O(1) space
def twoNumberSum4(arr, sum):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left < right:
        currentSum = arr[left] + arr[right]
        if currentSum == sum:
            return [arr[left], arr[right]]
        elif currentSum < sum:
            left += 1
        elif currentSum > sum:
            right -= 1
    return []


# Return index of the number

def twoSum(nums, target):
    left = 0
    right = len(nums) - 1
    list1 = copy.copy(nums)
    nums.sort()
    while left < right:
        if nums[left] + nums[right] == target:
            return [list1.index(nums[left]), list1.index(nums[right])]
        elif nums[left] + nums[right] > target:
            right = right - 1
        elif nums[left] + nums[right] < target:
            left = left + 1
    return []


def twoSum2(nums, target):
    dict1 = {}
    for num in range(len(nums)):
        check = target - nums[num]
        if str(check) in dict1.keys():
            return [dict1[str(check)], num]
        else:
            dict1[str(nums[num])] = num
    return []


print(twoSum([3, 2, 4], 6))

print(twoSum([3, 3], 6))


print(twoNumberSum1([4, 6], 10))
print(twoNumberSum1([4, 4], 10))

print(twoNumberSum2([4, 6], 10))
print(twoNumberSum2([4, 4], 10))

print(twoNumberSum3([4, 6], 10))
print(twoNumberSum3([4, 4], 10))

print(twoNumberSum4([4, 6], 10))
print(twoNumberSum4([4, 4], 10))
