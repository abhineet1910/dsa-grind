class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums.sort()

        current_len = 1
        max_len = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current_len += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                max_len = max(max_len, current_len)
                current_len = 1

        max_len = max(max_len, current_len)

        return max_len
        
        

        """
        :type nums: List[int]
        :rtype: int
        """
        