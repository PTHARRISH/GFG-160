# Maximum Subarray Sum
# Kadane's Algorithm (Best Approach)
def maxSubarraySum(arr):
    n = len(arr)
    res = arr[0]
    max_end = arr[0]
    for i in range(1, n):
        max_end = max(max_end + arr[i], arr[i])
        res = max(res, max_end)

    return res


# real world example:  Gaming/Scoring Systems,
#                      GitHub Contribution Streak Tracker

# Time Complexity: O(n)
# Single pass through the array -
# We visit each element exactly once

# Constant operations -
# Each iteration performs only basic arithmetic and comparison operations

# Linear growth -
#  As array size doubles, time taken doubles

# Optimal for this problem -
# Can't solve maximum subarray in less than O(n) time

# Space Complexity: O(1)
# Constant extra space -
# Only uses 3 variables (res, max_end, array length)

# No additional data structures -
# No extra arrays, stacks, or recursive call stack

# Space-efficient -
# Memory usage doesn't grow with input size

# In-place algorithm -
# Doesn't modify the original array


# Iterative method
def maxSubarraySum(arr):
    n = len(arr)
    res = arr[0]
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum = curr_sum + arr[j]
            res = max(res, curr_sum)
    return res


arr = [2, 3, -8, 7, -1, 2, 3]
print(maxSubarraySum(arr))
