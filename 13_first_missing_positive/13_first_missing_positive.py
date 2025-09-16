# Find the first missing positive integer in an unsorted integer array.
# Best Approach:
def missing_positive(arr):
    n = len(arr)
    for i in range(n):
        while i <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:
            temp = arr[i]
            arr[i] = arr[temp - 1]
            arr[temp - 1] = temp
    for i in range(n):
        if arr[i] != i + 1:
            return i + 1
    return n + 1

# Visited array approach
def missing_positive(arr):
    n = len(arr)
    vis = [False] * n
    for i in range(n):
        if 0 < arr[i] <= n:
            vis[arr[i] - 1] = True
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
