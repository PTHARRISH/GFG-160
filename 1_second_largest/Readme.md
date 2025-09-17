# Second Largest Element in Array

This document explains three approaches to find the **second largest element** in an array using Python. Each method includes a step-by-step walkthrough, showing how variables are updated and how the algorithm works.

---

## Approach 1: Single Iteration (Best Method)

### Debugger Walkthrough

- **Step 1:** Initialize `first` and `second` to negative infinity.
- **Step 2:** For each element in the array:
    - If the element is greater than `first`, update `second` to `first`, then set `first` to the element.
    - Else if the element is greater than `second` and not equal to `first`, update `second`.
    - The debugger prints the values of `first` and `second` after each iteration.
- **Step 3:** After the loop:
    - If `second` is still negative infinity, return `-1` (no second largest found).
    - Otherwise, return `second`.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

---

## Approach 2: Two Iterations

### Debugger Walkthrough

- **Step 1:** First loop finds the largest element (`first`).
- **Step 2:** Second loop finds the largest element not equal to `first` (`second`).
    - The debugger prints `first` after the first loop and updates `second` in the second loop.
- **Step 3:** If `second` is negative infinity, return `-1`. Otherwise, return `second`.

**Time Complexity:** O(2n)  
**Space Complexity:** O(1)

---

## Approach 3: Using `sorted()`

### Debugger Walkthrough

- **Step 1:** Sort the array.
- **Step 2:** Find the maximum (`first`).
- **Step 3:** Traverse from the end to find the largest element not equal to `first` (`second`).
    - The debugger prints the sorted array and updates `second` when found.
- **Step 4:** If `second` is negative infinity, return `-1`. Otherwise, return `second`.

**Time Complexity:** O(n log n)  
**Space Complexity:** O(1)

---

## What You Learned

- **Single Pass Efficiency:** The debugger shows how both largest and second largest are tracked in one pass.
- **Handling Duplicates:** All approaches correctly handle duplicate values.
- **Extensibility:** The single pass method can be extended to find third, fourth largest, etc.
- **Use Cases:** Ranking systems, leaderboards, stock analysis, and more.

---

## Summary Table

| Approach         | Time Complexity | Space Complexity | Key Idea         |
| ---------------- | -------------- | --------------- | --------------- |
| Single Iteration | O(n)           | O(1)            | Track two maxes |
| Two Iterations   | O(2n)          | O(1)            | Separate passes |
| Sorted           | O(n log n)     | O(1)            | Sort & scan     |

---

## Real World Applications

- **Ranking Systems:** Find the second highest score or salary.
- **Leaderboards:** Identify runner-up positions in competitions.
- **Stock Analysis:** Determine the second highest stock price.
- **Data Analysis:** Extend to find Kth largest or smallest elements.
- **Resource Allocation:** Useful in scheduling and prioritization tasks.

---

## How to Use

- Call any function with your array.
- The debugger will show variable updates at each step.
- All methods return the second largest element, or `-1` if not found.
- The single iteration method is fastest and most memory efficient.
