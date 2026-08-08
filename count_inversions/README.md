## Count Inversions of an Array

### Problem

Given an integer array `arr[]`, count the number of pairs `(i, j)` such that:

```text
i < j AND arr[i] > arr[j]



Input:  [4, 3, 2, 1]
Output: 6

Inversions:
(4,3), (4,2), (4,1),
(3,2), (3,1),
(2,1)
```
<p></p>
Brute Force:
Check every pair → O(n²)

Optimal:
Use Merge Sort to count inversions during merging → O(n log n)