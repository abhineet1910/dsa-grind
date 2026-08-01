class Solution(object):
    def sortColors(self, nums):
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        n = len(nums)
        # better approch 
        # cout0=0
        # cout1=0
        # cout2=0
        # n = len(nums)
        # for i in range (n):
        #     if nums[i]==0:
        #         cout0+=1
        #     elif nums[i]==1:
        #         cout1+=1
        #     else:
        #         cout2+=1
        # for i in range(0,cout0):
        #     nums[i]=0
        # for i in range (cout0,cout0+cout1):
        #     nums[i]=1
        # for i in range (cout0+cout1,n):
        #     nums[i]=2
        
    #  optimal approch will be 
        low = 0 
        mid = 0 
        high = n-1
        while mid<=high:
            if nums[mid]==0:
                swap(low,mid)
                low += 1
                mid += 1
            elif nums[mid]==1:
                mid += 1
            elif nums[mid]==2:
                swap(mid,high)
                high -=1
            
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        