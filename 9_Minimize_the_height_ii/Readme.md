# Minimize the Height II

This document explains the best approach to solve the **Minimize the Height II** problem in Python. The objective is to minimize the difference between the maximum and minimum heights after modifying each element by either increasing or decreasing it by a fixed value `k`.

---

## Best Approach: Sorting and Greedy

### Debugger Walkthrough

- **Step 1:** Sort the array.
- **Step 2:** Initialize `res` as the difference between the largest and smallest elements.
- **Step 3:** For each index `i` from 1 to `n-1`:
    - If subtracting `k` from `arr[i]` results in a negative value, skip this index.
    - Calculate the minimum height (`minh`) as the minimum of the smallest element plus `k` and the current element minus `k`.
    - Calculate the maximum height (`maxh`) as the maximum of the previous element plus `k` and the largest element minus `k`.
    - Update `res` with the minimum of its current value and `maxh - minh`.
    - The debugger prints the current `minh`, `maxh`, and `res` at each step.
- **Step 4:** Return `res` as the minimized difference.

---

## What You Learned

- **Sorting:** The debugger shows how sorting helps in efficiently comparing the modified heights.
- **Greedy Choice:** The debugger demonstrates how to choose the best split point to minimize the difference.
- **Time Complexity:** The debugger confirms the algorithm sorts the array and then makes a single pass.
- **Space Complexity:** The debugger highlights that only a constant amount of extra space is used.

---

## Summary Table

| Approach         | Time Complexity | Space Complexity | Key Idea         |
| ---------------- | --------------- | ---------------- | --------------- |
| Sorting + Greedy | O(n log n)      | O(1)             | Min/Max updates |

---

## Real World Applications

- **Building Construction:** Adjusting the heights of buildings to minimize skyline variation.
- **Resource Allocation:** Distributing resources to minimize the gap between the most and least allocated.
- **Exam Grading:** Moderating scores to reduce the difference between the highest and lowest marks.
- **Inventory Management:** Balancing stock levels across warehouses.
- **Scheduling:** Minimizing the difference in workloads among employees.

---

## How to Use

- Call the function with your array and value of `k`.
- The debugger will show the updates to minimum and maximum heights at each step.
- The function returns the minimized difference between the highest and lowest values after modification.

---

## Example

```python
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
print(ans)  # Output: 11
```

---
