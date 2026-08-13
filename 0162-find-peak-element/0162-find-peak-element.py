class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)
        low = 0
        high = n -1
        while low < high:
            mid = (low+ high)//2
            if nums[mid]>nums[mid+1]:
                high = mid
            else:
                low = mid + 1
        return high
        """
        :type nums: List[int]
        :rtype: int
        """
        