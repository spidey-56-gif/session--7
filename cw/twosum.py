# Time Complexity: O(n^2)
# Space Complexity: O(1)

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Test Executions
print("Test A:", twoSum([2, 7, 11, 15], 9))
print("Test B:", twoSum([3, 2, 4], 6))
print("Test C:", twoSum([3, 3], 6))
