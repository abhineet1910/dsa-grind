class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max1=0
        n = len(nums)
        cnt=0
        for i in range(n):
            if nums[i]==1:
                cnt += 1
                max1 = max(max1,cnt)
            else:
                cnt = 0
        return max1
        """
        :type nums: List[int]
        :rtype: int
        """
        