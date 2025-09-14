# Maximum Circular Subarray Sum

This document explains two approaches to solve the **Maximum Circular Subarray Sum** problem in Python. The goal is to find the largest sum of a subarray, considering the array as circular (i.e., after the last element, it wraps around to the first).

---

## Approach 1: Single Loop (Kadane’s Algorithm + Min Subarray)

### Debugger Walkthrough

- **Step 1:** Start with variables: `max_sum`, `min_sum`, `curr_max`, `curr_min`, and `total`.
- **Step 2:** For each element in the array:
  - The debugger shows `curr_max` updated to be either the current element or `curr_max + element` (whichever is larger).
  - `max_sum` is updated if `curr_max` is greater than previous `max_sum`.
  - Similarly, `curr_min` is updated to be either the current element or `curr_min + element` (whichever is smaller).
  - `min_sum` is updated if `curr_min` is smaller than previous `min_sum`.
  - `total` accumulates the sum of all elements.
  - At each iteration, the debugger prints the values of all these variables.
- **Step 3:** After the loop:
  - The debugger calculates `normal` (the max subarray sum without wrapping).
  - It calculates `circular` (the max sum with wrapping: `total - min_sum`).
  - If all numbers are negative, the debugger notes that `circular` would be zero, so it returns `normal`.
  - Otherwise, it returns the maximum of `normal` and `circular`.

---

## Approach 2: Two Loops (Suffix & Prefix)

### Debugger Walkthrough

- **Step 1:** Initialize a suffix sum array and a variable for suffix sums.
- **Step 2:** First loop (right to left):
  - The debugger updates the suffix sum for each index.
  - It records the maximum suffix sum at each step.
  - The debugger prints the suffix sum array after this loop.
- **Step 3:** Second loop (left to right):
  - The debugger uses Kadane’s algorithm to track the normal max subarray sum.
  - It accumulates the prefix sum.
  - At each index, the debugger combines the prefix sum and the corresponding suffix sum to check for a circular sum.
  - The debugger prints the current prefix, suffix, and the best circular sum found so far.
- **Step 4:** After both loops:
  - The debugger compares the best circular sum and the normal max subarray sum, returning the larger.

---

## What You Learned

- **Kadane’s Algorithm:** The debugger shows how it updates the running max subarray sum at each step.
- **Circular Subarray:** The debugger demonstrates how prefix and suffix sums are combined for wrap-around cases.
- **Time Complexity:** The debugger confirms only one or two passes through the array.
- **Space Complexity:** The debugger highlights the use of extra arrays or variables.
- **Dropping Constants:** The debugger ignores fixed multipliers and focuses on how the algorithm scales.

---

## Summary Table

| Approach    | Time Complexity | Space Complexity | Key Idea              |
| ----------- | --------------- | ---------------- | --------------------- |
| Single Loop | O(n)            | O(1)             | Kadane + min subarray |
| Two Loops   | O(n)            | O(n)             | Prefix + Suffix sums  |

---

## Real World Applications

- **Network Traffic Analysis:** Find the time window with the highest data transfer in a cyclic log (e.g., over 24 hours).
- **Sensor Data Monitoring:** Detect periods of maximum activity in circular sensor readings (e.g., temperature, pressure).
- **Game Development:** Calculate the best scoring streak in games with wrap-around levels or circular maps.
- **Financial Analysis:** Identify the most profitable consecutive days in a repeating cycle (e.g., weekly or monthly sales).
- **Scheduling:** Optimize resource allocation in cyclic schedules (e.g., shift planning, round-robin tournaments).
- **Circular DNA Analysis:** Locate regions with maximum gene expression in circular DNA sequences.

---

## How to Use

- Run either function with your array.
- The debugger will show variable updates at each step.
- Both return the maximum circular subarray sum.
- The single loop is more space-efficient.
