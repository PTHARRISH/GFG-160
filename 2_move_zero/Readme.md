# Move Zeroes to End of Array

This document explains the most efficient approach to solve the **Move Zeroes to End** problem in Python. The goal is to rearrange the elements of an array so that all zeroes are moved to the end, while maintaining the relative order of non-zero elements.

---

## Best Approach: Two-Pointer In-Place Partitioning

### Code

```python
def pushZerosToEnd(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1
    return arr
```

---

### Debugger Walkthrough

- **Step 1:** Initialize `count = 0` to track the position for the next non-zero element.
- **Step 2:** Iterate through the array with index `i`.
  - If `arr[i]` is not zero, swap it with `arr[count]`.
  - Increment `count` to move the boundary for non-zero elements.
  - The debugger shows the array after each swap and the current value of `count`.
- **Step 3:** After the loop, all non-zero elements are at the front, and all zeroes are at the end.

---

## Algorithm Used

- **Technique:** Two-pointer approach with in-place swapping.
- **Time Complexity:** O(n) — single pass through the array.
- **Space Complexity:** O(1) — modifies the array in-place, no extra space.

---

## Why This Algorithm is Brilliant

- **Single Pass:** Only one traversal of the array.
- **In-Place:** No extra memory allocation.
- **Stable:** Maintains the relative order of non-zero elements.
- **Efficient:** Optimal time and space complexity.

---

## Where Can You Use This Approach?

### 1. Similar Problems

- **Move all negative numbers to end:** Change the condition to `if arr[i] >= 0:`.
- **Move all even numbers to front:** Use `if arr[i] % 2 == 0:`.
- **Move all vowels to end (for strings):** Use `if char not in 'aeiou':`.

### 2. Real-World Applications

- **Data Cleaning:** Remove or segregate null/empty values.
- **File Processing:** Separate valid and invalid records.
- **Game Development:** Partition active and inactive objects.
- **Database Operations:** Partition data by criteria.
- **Image Processing:** Separate foreground and background pixels.

---

## Alternative Approach

```python
def pushZerosToEnd(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while count < n:
        arr[count] = 0
        count += 1
    return arr
```
- **Time Complexity:** O(2n)
- **Space Complexity:** O(1)

---

## Summary Table

| Approach         | Time Complexity | Space Complexity | Key Idea                |
|------------------|----------------|------------------|-------------------------|
| Two-pointer swap | O(n)           | O(1)             | In-place partitioning   |
| Overwrite + fill | O(2n)          | O(1)             | Overwrite then fill 0's |

---

## How to Use

- Call `pushZerosToEnd(arr)` with your array.
- The function returns the array with all zeroes moved to the end.
- The process is efficient and preserves the order of non-zero elements.
