# 12.Maximum Circular Sum
# Best Approach - Single Loop
def maxCircularSum(arr):
    n = len(arr)
    current_max = 0
    current_min = 0
    min_sum = arr[0]
    max_sum = arr[0]
    total = 0
    for i in range(n):
        current_max = max(arr[i] + current_max, arr[i])
        max_sum = max(max_sum, current_max)
        current_min = min(arr[i] + current_min, arr[i])
        min_sum = min(min_sum, current_min)
        total += arr[i]
    normal = max_sum
    circular = total - min_sum
    if total == min_sum:
        return normal
    return max(circular, normal)


# Two loops approach
def maxCircularSum(arr):
    n = len(arr)  # length of the array
    suffix = arr[n - 1]  # initialize suffix with the last element
    max_suff = [0] * (n + 1)  # array to store maximum suffix sums [0,0,...,0]
    max_suff[n - 1] = arr[n - 1]  # last element is the max suffix sum for itself
    # Calculate maximum suffix sums from right to left
    for i in range(n - 2, -1, -1):  # from second last to first element
        suffix += arr[i]  # accumulate suffix sum
        max_suff[i] = max(
            suffix, max_suff[i + 1]
        )  # store the maximum suffix sum at index i
    circular = arr[0]
    normal = arr[0]
    current_sum = 0
    prefix = 0
    # Calculate maximum subarray sum using Kadane's algorithm and combine with suffix sums
    for i in range(n):  # iterate through the array
        current_sum = max(
            arr[i] + current_sum, arr[i]
        )  # max subarray sum ending at index i
        normal = max(current_sum, normal)  # overall max subarray sum
        prefix += arr[i]  # accumulate prefix sum
        circular = max(circular, prefix + max_suff[i + 1])  # max circular sum
    return max(circular, normal)  # return the maximum of circular and normal sums


# Time Complexity: O(n)+O(n) = O(n) because of two passes through the array
# Drop constant factors - O(n)
# Single pass through the array - O(n)
# Constant time operations - O(1)
# Linear growth - As array size doubles, time taken doubles
# Optimal for this problem - Can't solve maximum circular sum in less than O(n) times
