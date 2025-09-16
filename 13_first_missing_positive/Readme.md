# First Missing Positive

This document explains three approaches to solve the **First Missing Positive** problem in Python. The goal is to find the smallest missing positive integer in an unsorted integer array.

---

## Approach 1: In-Place Index Placement (Best Approach)

### Debugger Walkthrough

- **Step 1:** Initialize `n` as the length of the array.
- **Step 2:** For each index `i` in the array:
    - The debugger checks if `arr[i]` is in the range `[1, n]` and not already in its correct position.
    - If so, it swaps `arr[i]` with the element at its target position (`arr[arr[i] - 1]`).
    - The debugger prints the array after each swap.
- **Step 3:** After placement, iterate through the array:
    - The debugger checks if `arr[i] != i + 1`.
    - If found, returns `i + 1` as the missing positive.
- **Step 4:** If all positions are correct, returns `n + 1`.

---

## Approach 2: Visited Array

### Debugger Walkthrough

- **Step 1:** Initialize a boolean array `vis` of size `n` (all `False`).
- **Step 2:** For each element in the array:
    - If the value is in `[1, n]`, mark `vis[arr[i] - 1]` as `True`.
    - The debugger prints the `vis` array after each update.
- **Step 3:** Iterate through `vis`:
    - The debugger checks for the first `False` entry.
    - Returns its index + 1 as the missing positive.
- **Step 4:** If all are `True`, returns `n + 1`.

---

## Approach 3: Sorting

### Debugger Walkthrough

- **Step 1:** Sort the array.
- **Step 2:** Initialize `res = 1`.
- **Step 3:** For each number in the sorted array:
    - If `num == res`, increment `res`.
    - If `num > res`, break (missing positive found).
    - The debugger prints `res` at each step.
- **Step 4:** Returns `res` as the missing positive.

---

## What You Learned

- **Index Placement:** The debugger shows how elements are moved to their correct positions for O(1) space.
- **Visited Array:** The debugger demonstrates marking seen positives for easy lookup.
- **Sorting:** The debugger highlights how sorting helps track the next expected positive.
- **Time Complexity:** The debugger confirms O(n) for index/visited, O(n log n) for sorting.
- **Space Complexity:** The debugger notes O(1) for index, O(n) for visited, O(1) for sorting (if in-place).

---

## Summary Table

| Approach           | Time Complexity | Space Complexity | Key Idea                |
| ------------------ | --------------- | ---------------- | ----------------------- |
| Index Placement    | O(n)            | O(1)             | Place numbers in index  |
| Visited Array      | O(n)            | O(n)             | Mark seen positives     |
| Sorting            | O(n log n)      | O(1) / O(n)      | Track after sorting     |

---

## Real World Applications

- **Database Record Management:** Find the first available unique ID in a list of used IDs.
- **Inventory Tracking:** Identify the first missing SKU or product code in a sequence.
- **Scheduling:** Allocate the earliest available slot or resource.
- **Gaming:** Assign the lowest unused player or object ID.
- **Networking:** Find the first unused port or address in a range.
- **Data Cleaning:** Detect missing entries in sequential datasets.

---

## How to Use

- Run any function with your array.
- The debugger will show variable updates at each step.
- All return the smallest missing positive integer.
- The index placement approach is most efficient in time and space.
