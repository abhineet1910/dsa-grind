class Solution(object):
    def searchInsert(self, nums, target):
        n = len(nums)
        lb= -1
        low = 0
        high= n -1 
        while low<=high:
            mid = (low + high)//2
            # if target not in nums:
            #     if target>n:
                

            if nums[mid]>=target:
                lb = mid
                high = mid-1
            else:
                lb = mid +1
                low = mid +1 

        return lb   
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        