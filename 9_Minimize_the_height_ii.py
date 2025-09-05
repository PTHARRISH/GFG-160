# Best Approach
def getMinDiff(arr, k):
    arr.sort()
    n = len(arr)
    res = arr[n - 1] - arr[0]
    for i in range(1, n):
        if arr[i] - k < 0:
            continue

        minh = min(arr[0] + k, arr[i] - k)
        maxh = max(arr[i - 1] + k, arr[n - 1] - k)
        res = min(res, maxh - minh)

    return res


k = 6
arr = [12, 6, 4, 15, 17, 10]

ans = getMinDiff(arr, k)
print(ans)


# Time Complexity: O(nlogn), as we are sorting the array.
# Auxiliary Space: O(1)
