# Majority Element (More Than n/3)

This document explains how to solve the **Majority Element (More Than n/3)** problem in Python. The goal is to find all elements in an array that appear more than ⌊n/3⌋ times.

---

## Brute Force Approach

### Debugger Walkthrough

- **Step 1:** Initialize an empty dictionary `data` to count occurrences.
- **Step 2:** For each element in the array:
    - The debugger checks if the element is already in `data`.
    - If yes, it increments the count; otherwise, it sets the count to 1.
    - The debugger prints the current state of `data` after each update.
- **Step 3:** Calculate the threshold `t` as `n // 3`.
- **Step 4:** Iterate through the dictionary:
    - The debugger checks if the count for each key is greater than `t`.
    - If so, it adds the key to the `majority` list.
    - The debugger prints the current `majority` list.
- **Step 5:** Return the sorted `majority` list.

---

## Optimized Approach (Boyer-Moore Voting Algorithm)

### Debugger Walkthrough

- **Step 1:** Initialize two candidate variables and their counts.
- **Step 2:** First pass through the array:
    - The debugger updates candidates and counts based on the current element.
    - If the element matches a candidate, increment its count.
    - If a count is zero, assign the current element as the new candidate.
    - The debugger prints candidates and counts at each step.
- **Step 3:** Second pass to verify counts:
    - The debugger counts actual occurrences of the candidates.
    - If a candidate appears more than `n // 3` times, add it to the result.
    - The debugger prints the final result.

---

## What You Learned

- **Hash Map Counting:** The debugger shows how to use a dictionary to count occurrences efficiently.
- **Boyer-Moore Voting:** The debugger demonstrates how to track up to two majority candidates in a single pass.
- **Time Complexity:** Both approaches are O(n), but the optimized approach uses O(1) space.
- **Space Complexity:** The brute force approach uses O(n) space for the dictionary.

---

## Summary Table

| Approach         | Time Complexity | Space Complexity | Key Idea                |
| ---------------- | --------------- | ---------------- | ----------------------- |
| Brute Force      | O(n)            | O(n)             | Hash map counting       |
| Boyer-Moore      | O(n)            | O(1)             | Voting for candidates   |

---

## Real World Applications

- **Survey Analysis:** Identify popular choices that exceed a certain threshold in survey responses.
- **Database Optimization:** Detect frequently accessed records for caching.
- **Fraud Detection:** Find repeated patterns in transaction logs.
- **Recommendation Systems:** Highlight items that are trending among users.
- **Voting Systems:** Determine candidates with significant support in elections.

---

## How to Use

- Run the brute force or optimized function with your array.
- The debugger will show variable updates at each step.
- Both return a sorted list of majority elements.
- The optimized approach is more space-efficient.
