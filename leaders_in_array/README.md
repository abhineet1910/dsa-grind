# Leaders in an Array

## Problem
A leader is an element that is **greater than or equal to all the elements on its right**. The last element is always a leader.

### Example
```text
Input:  [16, 17, 4, 3, 5, 2]
Output: [17, 5, 2]
```

---

## Brute Force

### Idea
For each element, check every element on its right. If no greater element exists, it is a leader.

- **Time Complexity:** `O(N²)`
- **Space Complexity:** `O(1)` (excluding output)

---

## Optimal

### Idea
Traverse from **right to left** while maintaining the **maximum element seen so far (`maxRight`)**.

- Last element is always a leader.
- If `arr[i] >= maxRight`, it is a leader.
- Update `maxRight`.
- Reverse the result before returning.

- **Time Complexity:** `O(N)`
- **Space Complexity:** `O(1)` (excluding output)

---

## Key Takeaway

Instead of checking **all elements to the right**, keep track of the **maximum element on the right** while traversing backwards.