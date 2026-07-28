class Solution(object):
    def moveZeroes(self, nums):
        # brute force 

        # temp = []
        # n = len(nums)

        # # Store all non-zero elements
        # for i in range(n):
        #     if nums[i] != 0:
        #         temp.append(nums[i])

        
        # for i in range(len(temp)):
        #     nums[i] = temp[i]

        # for i in range(len(temp), n):
        #     nums[i] = 0
        # optimmal solution 
        insert = 0 
        n = len(nums)
        for i in range (0,n):
            if nums[i] != 0:
                nums[insert] = nums[i]
                insert += 1
        for i in range(insert,n):
            nums[i] = 0


        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        