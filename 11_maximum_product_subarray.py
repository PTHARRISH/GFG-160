def maxProduct(arr):
    # code here
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
