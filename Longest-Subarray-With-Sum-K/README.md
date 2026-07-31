# Longest Subarray With Sum K

## Problem Statement

Given an integer array `arr[]` and an integer `K`, find the **length of the longest subarray** whose sum is equal to `K`.

### Example

```text
Input:
arr = [2, 3, 5, 1, 9]
K = 10

Output:
3
```

---

## Approaches

### 1. Brute Force

**Idea:**
- Generate all possible subarrays.
- Maintain a running sum.
- Update the maximum length whenever the sum equals `K`.

**Time Complexity:** `O(N²)`  
**Space Complexity:** `O(1)`

---

### 2. Prefix Sum + HashMap (Better)

**Idea:**
- Maintain a running prefix sum.
- Store the first occurrence of each prefix sum in a HashMap.
- If `(prefixSum - K)` exists, a valid subarray is found.
- Update the maximum length.

**Time Complexity:** `O(N)`  
**Space Complexity:** `O(N)`

---

## Files

```text
Longest-Subarray-With-Sum-K/
├── brute_force.py
├── better_prefix_sum.py
└── README.md
```

---

## Concepts Used

- Arrays
- Subarrays
- Prefix Sum
- HashMap (Dictionary)
- Running Sum