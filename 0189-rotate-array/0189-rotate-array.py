class Solution(object):
    def rotate(self, nums, k):
    
        temp = [0] * k
        n = len(nums)
        k=k%n
        for i in range(k):
            temp[i] = nums[n - k + i]

        # Shift remaining elements to the right
        for i in range(n - k - 1, -1, -1):
            nums[i + k] = nums[i]

        # Copy saved elements to the front
        for i in range(k):
            nums[i] = temp[i]
        

        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        