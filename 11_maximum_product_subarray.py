# Best Approach
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
# Space Complexity: O(1)
# Constant extra space -
# Only uses a few variables (res, curr_sum, array length)

# No additional data structures -
# No extra arrays, stacks, or recursive call stack

# Space-efficient -
# Memory usage doesn't grow with input size

# In-place algorithm -
# Doesn't modify the original array
