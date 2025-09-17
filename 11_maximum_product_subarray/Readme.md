# 11. Maximum Product Subarray

This document explains three approaches to solve the **Maximum Product Subarray** problem in Python. The goal is to find the largest product of a contiguous subarray within a given array.

---

## Approach 1: Best Approach (Two Passes)

### Debugger Walkthrough

- **Step 1:** Initialize `max_pro` as negative infinity, and two variables `lefttoright` and `righttoleft` as 1.
- **Step 2:** For each index `i` in the array:
    - If `lefttoright` or `righttoleft` becomes 0, reset it to 1.
    - Multiply `lefttoright` by the current element from the left.
    - Multiply `righttoleft` by the current element from the right.
    - Update `max_pro` with the maximum of itself, `lefttoright`, and `righttoleft`.
    - The debugger prints the current values of `lefttoright`, `righttoleft`, and `max_pro` at each step.
- **Step 3:** Return `max_pro` as the result.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

---

## Approach 2: Greedy (Dynamic Programming)

### Debugger Walkthrough

- **Step 1:** Initialize `res`, `max_end`, and `min_end` with the first element.
- **Step 2:** For each element from the second to the last:
    - Calculate the temporary maximum product (`temp`) as the max of the current element, `max_end * element`, and `min_end * element`.
    - Update `min_end` as the min of the current element, `max_end * element`, and `min_end * element`.
    - Set `max_end` to `temp`.
    - Update `res` if `max_end` is greater.
    - The debugger prints `max_end`, `min_end`, and `res` at each iteration.
- **Step 3:** Return `res` as the result.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

---

## Approach 3: Iterative (Brute Force)

### Debugger Walkthrough

- **Step 1:** Initialize `res` with the first element.
- **Step 2:** For each starting index `i`:
    - Set `curr_pro` to 1.
    - For each ending index `j` from `i` to the end:
        - Multiply `curr_pro` by `arr[j]`.
        - Update `res` if `curr_pro` is greater.
        - The debugger prints `curr_pro` and `res` at each step.
- **Step 3:** Return `res` as the result.

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

---

## What You Learned

- **Two Passes:** Handles negative numbers and zeros by traversing from both ends.
- **Dynamic Programming:** Tracks both max and min products due to negative numbers.
- **Brute Force:** Checks all possible subarrays, but is inefficient for large arrays.
- **Time Complexity:** Only the first two approaches are optimal for large inputs.
- **Space Complexity:** All approaches use constant extra space.

---

## Summary Table

| Approach     | Time Complexity | Space Complexity | Key Idea                  |
| ------------ | --------------- | ---------------- | ------------------------- |
| Two Passes   | O(n)            | O(1)             | Left & right traversal    |
| Greedy/DP    | O(n)            | O(1)             | Track max/min products    |
| Brute Force  | O(n²)           | O(1)             | All subarrays             |

---

## Real World Applications

- **Stock Analysis:** Find the period with the highest product of returns.
- **Signal Processing:** Detect the segment with the strongest multiplicative signal.
- **Genomics:** Identify regions with the highest product of gene expression levels.
- **Finance:** Analyze periods of compounding growth or loss.
- **Physics:** Locate intervals with maximum energy transfer in a sequence.

---

## How to Use

- Run any of the provided functions with your array.
- The debugger will show variable updates at each step.
- All return the maximum product subarray.
- The first two approaches are optimal for large arrays.
