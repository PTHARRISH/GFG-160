# Best Approach (3rd method)
def pushZerosToEnd(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1
    return arr


# Algorithm Used: 
# Two-Pointer Technique (In-Place Partitioning)

# Type: 
# Two-pointer approach with in-place swapping
# Time Complexity: O(n) - single pass through array
# Space Complexity: O(1) - modifies array in-place, no extra space

# Why This Algorithm is Brilliant
# Advantages:
# Single Pass: Only goes through array once
# In-Place: No extra memory needed
# Stable: Maintains relative order of non-zeros
# Efficient: Optimal time and space complexity

# Where Can You Use This Approach?
# 1. Similar Problems:

# # Move all negative numbers to end
# if arr[i] >= 0:  # Keep positive numbers at front

# # Move all even numbers to front  
# if arr[i] % 2 == 0:  # Keep even numbers at front

# # Move all vowels to end (for strings)
# if char not in 'aeiou':  # Keep consonants at front

# 2. Real-World Applications:
# Data Cleaning: Remove null/empty values

# File Processing: Separate valid/invalid records

# Game Development: Separate active/inactive objects

# Database Operations: Partition data by criteria

# Image Processing: Separate foreground/background pixels


# def pushZerosToEnd(arr):
#     count = 0
#     n = len(arr)
#     for i in range(n):
#         if arr[i] != 0:
#             arr[count] = arr[i]
#             count += 1
#     while count < n:
#         arr[count] = 0
#         count += 1
#     return arr


# T.C = O(2n)
# S.C = O(1)
