class Solution:
    def longestSubarray(self, arr, k):
        prefix = 0
        max_len = 0
        prefix_map = {}

        for i in range(len(arr)):
            prefix += arr[i]

            # Case 1: subarray starts from index 0
            if prefix == k:
                max_len = max(max_len, i + 1)

            # Case 2: subarray starts after index 0
            if (prefix - k) in prefix_map:
                length = i - prefix_map[prefix - k]
                max_len = max(max_len, length)

            # Store only the first occurrence
            if prefix not in prefix_map:
                prefix_map[prefix] = i

        return max_len
arr1 = [1,1,9,8,1,1]

k = 10
sol = Solution()
longest_subarray = sol.longestSubarray(arr1, k)
print(longest_subarray)