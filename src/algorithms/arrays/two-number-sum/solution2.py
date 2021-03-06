# STRATEGY:
# Use hash table/dict to store read values
# COMPLEXITY:
# O(n) time | O(n) space

def twoNumberSum(array, targetSum):
    nums = {}
    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []
