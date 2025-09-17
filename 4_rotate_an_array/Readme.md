# 4. Rotate an Array

This document explains multiple approaches to solve the **Rotate an Array** problem in Python. The goal is to rotate the elements of an array to the left by `d` positions.

---

## Approach 1: Reversal Algorithm (Best Approach)

### Debugger Walkthrough

- **Step 1:** Calculate the effective rotation `d %= n` to handle cases where `d > n`.
- **Step 2:** Reverse the first `d` elements.
- **Step 3:** Reverse the remaining `n-d` elements.
- **Step 4:** Reverse the entire array.
- The debugger shows the array after each reversal step.
- **Step 5:** Return the rotated array.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

---

## Approach 2: Slicing

### Debugger Walkthrough

- **Step 1:** Calculate `d %= n`.
- **Step 2:** Use array slicing to create a new array: `arr[d:] + arr[:d]`.
- The debugger prints the sliced arrays and the final result.
- **Step 3:** Return the new rotated array.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

---

## Approach 3: Temporary Array

### Debugger Walkthrough

- **Step 1:** Create an empty temporary array.
- **Step 2:** Append elements from index `d` to `n-1`.
- **Step 3:** Append elements from index `0` to `d-1`.
- The debugger prints the temporary array after each step.
- **Step 4:** Return the temporary array.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

---

## Approach 4: Rotate One by One

### Debugger Walkthrough

- **Step 1:** Repeat `d` times:
    - Store the first element.
    - Shift all elements left by one.
    - Place the stored element at the end.
    - The debugger prints the array after each rotation.
- **Step 2:** Return the rotated array.

**Time Complexity:** O(d*n)  
**Space Complexity:** O(1)

---

## What You Learned

- **Reversal Algorithm:** Efficient in-place rotation using three reversals.
- **Slicing:** Simple and concise, but uses extra space.
- **Temporary Array:** Explicitly constructs the rotated array.
- **One by One:** Intuitive but inefficient for large `d`.

---

## Summary Table

| Approach           | Time Complexity | Space Complexity | Key Idea         |
| ------------------ | --------------- | ---------------- | ---------------- |
| Reversal Algorithm | O(n)            | O(1)             | Three reversals  |
| Slicing            | O(n)            | O(n)             | Array slicing    |
| Temporary Array    | O(n)            | O(n)             | Extra array      |
| One by One         | O(d*n)          | O(1)             | Shift elements   |

---

## Real World Applications

- **Data Buffering:** Rotate logs or data streams for cyclic buffers.
- **Scheduling:** Shift time slots or tasks in round-robin scheduling.
- **Cryptography:** Simple ciphers using array rotations.
- **Image Processing:** Rotate pixel arrays for transformations.
- **Game Development:** Rotate player turns or board states.

---

## How to Use

- Choose an approach based on your space and time requirements.
- Call the function with your array and rotation count `d`.
- The debugger (print statements) will show intermediate steps.
- All approaches return the rotated array.
