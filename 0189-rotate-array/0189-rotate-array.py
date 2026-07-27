class Solution(object):
    def rotate(self, nums, k):
    
        
        n = len(nums)
        k=k%n
        
        def reverse(l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l += 1
                r -= 1
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        
        # for i in range(k):
        #     temp[i] = nums[n - k + i]

        # # Shift remaining elements to the right
        # for i in range(n - k - 1, -1, -1):
        #     nums[i + k] = nums[i]

        # # Copy saved elements to the front
        # for i in range(k):
        #     nums[i] = temp[i]
        

        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        