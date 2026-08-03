class Solution(object):
    def nextPermutation(self, nums):
        index = -1
        n = len(nums)
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                index = i
                break
        if index == -1:
            self.reverse(nums, 0, n - 1)
            return
        for i in range(n-1,index,-1):
            if (nums[i]>nums[index]):
                nums[i],nums[index]=nums[index],nums[i]
                break
        self.reverse(nums, index + 1, n - 1)

    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        