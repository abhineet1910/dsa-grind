class Solution(object):
    def sortColors(self, nums):
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]
        # better approch 
        cout0=0
        cout1=0
        cout2=0
        n = len(nums)
        for i in range (n):
            if nums[i]==0:
                cout0+=1
            elif nums[i]==1:
                cout1+=1
            else:
                cout2+=1
        for i in range(0,cout0):
            nums[i]=0
        for i in range (cout0,cout0+cout1):
            nums[i]=1
        for i in range (cout0+cout1,n):
            nums[i]=2
        

        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        