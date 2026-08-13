class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        low = 0 
        high = n - 1
        while low < high:
            mid = (low+high)//2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]
        """
        :type nums: List[int]
        :rtype: int
        """
        