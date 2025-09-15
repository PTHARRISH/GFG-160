# Find the first missing positive integer in an unsorted integer array.
# Best Approach:

# Visited array approach
def missing_positive(arr):
    n = len(arr)
    vis = [False] * n
    for i in range(n):
        if 0 < arr[i] <= n:
            vis[arr[i]-1] = True
    for i in range(1, n + 1):
        if not vis[i - 1]:
            return i
    return n + 1


# Loop through the array and sort it.
def missing_positive(arr):
    n = len(arr)
    res = 1
    arr.sort()

    for num in arr:
        if num == res:
            res += 1
        elif num > res:
            break
    return res
