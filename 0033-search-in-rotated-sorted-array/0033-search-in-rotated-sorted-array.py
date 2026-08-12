class Solution(object):
    def search(self, nums, target):
        n =  len(nums)
        low = 0 
        high = n -1 
        while low<=high:
            mid = (low +high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] <= nums[high]:
                if nums[mid]<=target<=nums[high]:
                    low = mid +1
                else :
                    high = mid - 1
            else:
                if nums[low]<=target<=nums[mid]:
                    high = mid - 1
                else:
                    low = mid +1
        return -1   
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        