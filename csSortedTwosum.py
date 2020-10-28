# Given a sorted array (in ascending order) of integers and a target, write a function that finds the two integers that add up to the target.

# Examples:

# csSortedTwoSum([3,8,12,16], 11) -> [0,1]
# csSortedTwoSum([3,4,5], 8) -> [0,2]
# csSortedTwoSum([0,1], 1) -> [0,1]
# Notes:

# Each input will have exactly one solution.
# You may not use the same element twice.

def csSortedTwoSum(numbers, target):
    for i in range(len(numbers)):
        for j in range (i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i, j]
    return "no valid solution found"



print(csSortedTwoSum([3,7,12,16], 11)) ## should bwe [0, 1]