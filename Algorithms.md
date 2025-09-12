# Algorithms in Data Structures and Algorithms (DSA)

## What is DSA?
**DSA** stands for **Data Structures and Algorithms**.  
- **Data Structures**: Ways to organize and store data efficiently.
- **Algorithms**: Step-by-step procedures to solve problems.

## Why DSA?
- Improves problem-solving skills.
- Optimizes code for speed and memory.
- Essential for technical interviews and real-world applications.

## How DSA?
- Learn basic data structures (arrays, lists, stacks, queues, trees, graphs).
- Understand common algorithms (searching, sorting, traversal).
- Practice analyzing and optimizing code.

---

## Time Complexity & Space Complexity

| Complexity Type | Definition | How to Calculate | Example |
|-----------------|------------|------------------|---------|
| Time Complexity | Measures the amount of time an algorithm takes as input size grows. | Count the number of basic operations as a function of input size `n`. | Traversing an array of size `n` is `O(n)` |
| Space Complexity | Measures the amount of memory an algorithm uses as input size grows. | Count the extra space used (not including input). | Using an extra array of size `n` is `O(n)` |

### Example
```python
def sum_array(arr):
    total = 0          # O(1) space
    for num in arr:    # O(n) time
        total += num
    return total
```
- **Time Complexity**: O(n) (one pass through array)
- **Space Complexity**: O(1) (no extra space except variables)

---

## Types of Time Complexity

| Type         | Notation | Example | Description |
|--------------|----------|---------|-------------|
| Constant     | O(1)     | Accessing arr[0] | Time doesn't depend on input size |
| Linear       | O(n)     | Traversing array | Time grows proportionally with input size |
| Logarithmic  | O(log n) | Binary Search | Time grows slowly as input increases |
| Quadratic    | O(n²)    | Nested loops | Time grows with square of input size |
| Exponential  | O(2ⁿ)    | Recursive Fibonacci | Time doubles with each increase in input |

### Examples
- **Constant**: `x = arr[0]`
- **Linear**: `for x in arr: print(x)`
- **Logarithmic**: Binary search in sorted array
- **Quadratic**: `for i in arr: for j in arr: print(i, j)`
- **Exponential**: Recursive solution to Fibonacci

---

## Dropping Constants

- In Big O notation, constants are ignored.
- Example: `O(2n)` becomes `O(n)`.
- **Why?**: As `n` grows, constants have negligible effect.

### Deep Example
```python
def double_traverse(arr):
    for i in arr:      # O(n)
        print(i)
    for j in arr:      # O(n)
        print(j)
```
- Total operations: `2n`
- Big O: `O(n)` (drop constant 2)

---

## Dropping Non-Dominant Terms

- Only the fastest-growing term matters.
- Example: `O(n² + n)` becomes `O(n²)`.
- **Why?**: For large `n`, `n²` dominates `n`.

### Deep Example
```python
def mixed_loops(arr):
    for i in arr:           # O(n)
        print(i)
    for i in arr:
        for j in arr:       # O(n²)
            print(i, j)
```
- Total: `n + n²`
- Big O: `O(n²)` (drop non-dominant `n`)

---

## Loop Calculations

### Example 1: Single Loop
```python
for i in range(n):   # O(n)
    print(i)
```

### Example 2: Nested Loop
```python
for i in range(n):       # O(n)
    for j in range(n):   # O(n)
        print(i, j)      # O(n²)
```

### Example 3: Logarithmic Loop
```python
i = 1
while i < n:
    print(i)
    i *= 2              # O(log n)
```

---

## Common Algorithms

### 1. Single Pass Linear Search
- **Description**: Search for an element by checking each item once.
- **Time Complexity**: O(n)
- **Example**:
    ```python
    def linear_search(arr, target):
        for i in arr:
            if i == target:
                return True
        return False
    ```

### 2. Two-Pointer Technique
- **Description**: Use two indices to scan or compare elements in a sequence.
- **Time Complexity**: O(n)
- **Example**:
    ```python
    def two_sum(arr, target):
        left, right = 0, len(arr) - 1
        while left < right:
            s = arr[left] + arr[right]
            if s == target:
                return True
            elif s < target:
                left += 1
            else:
                right -= 1
        return False
    ```

### 3. Kadane's Algorithm
- **Description**: Finds the maximum sum subarray in O(n) time.
- **Time Complexity**: O(n)
- **Example**:
    ```python
    def kadane(arr):
        max_sum = curr_sum = arr[0]
        for num in arr[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        return max_sum
    ```
### 4. Greedy Approach
- **Description**: Makes the locally optimal choice at each step with the hope of finding a global optimum.
- **Time Complexity**: Varies (often O(n) or O(n log n))
- **Example**:
    ```python
    def coin_change(coins, amount):
        coins.sort(reverse=True)
        count = 0
        for coin in coins:
            while amount >= coin:
                amount -= coin
                count += 1
        return count if amount == 0 else -1
    ```
---

## Summary Table

| Algorithm                | Technique        | Time Complexity | Space Complexity | Use Case                |
|--------------------------|-----------------|-----------------|------------------|-------------------------|
| Linear Search            | Single Pass     | O(n)            | O(1)             | Find element in array   |
| Two-Pointer Technique    | Two Indices     | O(n)            | O(1)             | Pair sum, reverse array |
| Kadane's Algorithm       | Dynamic Update  | O(n)            | O(1)             | Max subarray sum        |
