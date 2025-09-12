# 11.Maximum Product Subarray
# Best Approach
def maxProduct(arr):
    n = len(arr)
    max_pro = float("-inf")
    lefttoright = 1
    righttoleft = 1
    for i in range(n):
        if lefttoright == 0:
            lefttoright = 1
        elif righttoleft == 0:
            righttoleft = 1
        lefttoright *= arr[i]
        righttoleft *= arr[n - i - 1]
        max_pro = max(max_pro, lefttoright, righttoleft)

    return max_pro


# Time Complexity: O(n)
# Single pass through the array - O(n)
# Constant time operations - O(1)
# Linear growth - As array size doubles, time taken doubles
# Optimal for this problem - Can't solve maximum product subarray in less than O(n) time


# Greedy Approach
def maxProduct(arr):
    n = len(arr)
    res = arr[0]
    max_end = arr[0]
    min_end = arr[0]
    for i in range(1, n):
        temp = max(arr[i], max_end * arr[i], min_end * arr[i])
        min_end = min(arr[i], max_end * arr[i], min_end * arr[i])
        max_end = temp
        res = max(res, max_end)
    return res


# Iterative method
def maxProduct(arr):
    n = len(arr)
    res = arr[0]
    for i in range(n):
        curr_pro = 1
        for j in range(i, n):
            curr_pro = curr_pro * arr[j]
            res = max(res, curr_pro)
    return res


arr = [-1, -3, -10, 0, 6]
print(maxProduct(arr))


# Time Complexity: O(n^2)
# Two nested loops -
# Outer loop runs n times, inner loop runs up to n times
# Quadratic growth -
# As input size doubles, time taken increases by a factor of four
# Not optimal for large inputs -
# Becomes impractical for large arrays

# Note:
# There is a more optimal O(n) solution using dynamic programming
# for the maximum product subarray problem.
# Space Complexity: O(1)
# Constant extra space -
# Only uses a few variables (res, curr_sum, array length)

# No additional data structures -
# No extra arrays, stacks, or recursive call stack

# Space-efficient -
# Memory usage doesn't grow with input size

# In-place algorithm -
# Doesn't modify the original array
