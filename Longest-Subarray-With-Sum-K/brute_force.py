class Solution:
    def longestSubarray(self, arr, k):
        n = len(arr)
        max_len = 0

        for i in range(n):
            current_sum = 0

            for j in range(i, n):
                current_sum += arr[j]

                if current_sum == k:
                    max_len = max(max_len, j - i + 1)

        return max_len
arr1 = [-1,-3,-4,-2,1,1,9,8,1,1]
# print(len(arr1))
# print(sum([-1,-3,-4,-2]))
k = 10
sol = Solution()
longest_subarray = sol.longestSubarray(arr1, k)
print(longest_subarray)