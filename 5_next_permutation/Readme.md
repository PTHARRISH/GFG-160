# Next Permutation of a Given Array of Numbers

This document explains the optimal approach to solve the **Next Permutation** problem in Python. The goal is to rearrange numbers into the lexicographically next greater permutation. If such arrangement is not possible, it rearranges it as the lowest possible order (i.e., sorted in ascending order).

---

## Best Approach: Single Pass from Right

### Debugger Walkthrough

- **Step 1:** Start from the end of the array and look for the first index (`pivot`) where `arr[i] < arr[i+1]`.
    - The debugger highlights the search for the pivot.
- **Step 2:** If no such index exists (the array is in descending order), reverse the entire array.
    - The debugger shows the reversed array.
- **Step 3:** Otherwise, find the smallest element greater than `arr[pivot]` to the right of `pivot` and swap them.
    - The debugger prints the swap operation.
- **Step 4:** Reverse the subarray to the right of the pivot to get the next permutation.
    - The debugger shows the final array after reversal.
- **Step 5:** Return the modified array.

---

## What You Learned

- **Pivot Identification:** The debugger demonstrates how to find the rightmost ascent.
- **Swap and Reverse:** The debugger shows how swapping and reversing ensures the next permutation.
- **Time Complexity:** The debugger confirms a single pass for both finding the pivot and reversing.
- **Space Complexity:** The debugger highlights that the operation is in-place (O(1) extra space).
- **Edge Cases:** The debugger handles cases where the array is already the highest permutation.

---

## Summary Table

| Approach      | Time Complexity | Space Complexity | Key Idea                |
| ------------- | --------------- | ---------------- | ----------------------- |
| Single Pass   | O(n)            | O(1)             | Pivot, swap, reverse    |

---

## Real World Applications

- **Generating Permutations:** Useful in algorithms that require generating permutations in order (e.g., combinatorial problems).
- **Puzzle Solvers:** Used in solving permutation-based puzzles (e.g., next state generation).
- **Scheduling:** Finding the next possible schedule or arrangement.
- **Game Development:** Generating next possible moves or states in games.
- **Cryptography:** Permutation generation for key scheduling or shuffling.

---

## How to Use

- Call the `nextPermutation` function with your array.
- The debugger will show each step: finding the pivot, swapping, and reversing.
- The function modifies the array in-place and returns the next permutation.
- Efficient for large arrays due to O(n) time and O(1) space.

---

## Example

```python
arr = [1, 2, 4, 5, 6, 0]
nextPermutation(arr)
print(arr)  # Output: [1, 2, 4, 6, 0, 5]
```

---

## Code

```python
def nextPermutation(arr):
        n = len(arr)
        pivot = -1
        for i in range(n - 2, -1, -1):
                if arr[i] < arr[i + 1]:
                        pivot = i
                        break
        if pivot == -1:
                arr.reverse()
                return
        for i in range(n - 1, pivot, -1):
                if arr[pivot] < arr[i]:
                        arr[pivot], arr[i] = arr[i], arr[pivot]
                        break
        left, right = pivot + 1, n - 1
        while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        return arr
```

---