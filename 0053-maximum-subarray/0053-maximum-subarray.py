class Solution(object):
    def maxSubArray(self, nums):
        maxsub=nums[0]
        cursub=0
        for n in nums:
            if cursub<0:
                cursub=0
            cursub += n
            maxsub=max(cursub,maxsub)
        return maxsub
        """
        :type nums: List[int]
        :rtype: int
        """
        