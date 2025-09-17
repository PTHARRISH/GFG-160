# 3. Reverse An Array

This document explains two approaches to solve the **Reverse an Array** problem in Python. The goal is to reverse the elements of an array in place or using extra space.

---

## Approach 1: Two Pointer (Best Approach)

### Debugger Walkthrough

- **Step 1:** Initialize two pointers: one at the start (`i = 0`) and one at the end (`n - 1 - i`).
- **Step 2:** For each iteration up to the middle of the array:
    - The debugger swaps the elements at the two pointers.
    - After each swap, the debugger prints the current state of the array.
    - The pointers move towards each other.
- **Step 3:** When the pointers meet or cross, the array is fully reversed.
- **Step 4:** The debugger returns the reversed array.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

---

## Approach 2: Naive Method (Using Extra Array)

### Debugger Walkthrough

- **Step 1:** Initialize an empty temporary array.
- **Step 2:** Loop through the original array from the end to the start:
    - The debugger appends each element to the temporary array.
    - After each append, the debugger prints the temporary array.
- **Step 3:** After the loop, the debugger returns the temporary array as the reversed array.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

---

## What You Learned

- **Two Pointer Technique:** Efficiently reverses the array in place by swapping elements from both ends.
- **Naive Method:** Uses extra space to build a reversed copy.
- **Time Complexity:** Both methods require a single pass through the array.
- **Space Complexity:** The two pointer approach is optimal in space.

---

## Summary Table

| Approach      | Time Complexity | Space Complexity | Key Idea         |
| ------------- | --------------- | ---------------- | ---------------- |
| Two Pointer   | O(n)            | O(1)             | In-place swap    |
| Naive         | O(n)            | O(n)             | Extra array copy |

---

## Real World Applications

- **Data Processing:** Reversing logs or records for chronological analysis.
- **Algorithm Design:** Used in palindrome checks, undo operations, and stack implementations.
- **Image Processing:** Flipping image rows or columns.
- **Game Development:** Reversing move sequences or animations.
- **Scheduling:** Reversing order of tasks or events.

---

## How to Use

- Call either function with your array.
- The debugger will show the array state at each step.
- Both return the reversed array.
- The two pointer approach is more space-efficient.
