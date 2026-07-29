class Solution(object):
    def missingNumber(self, nums):
        N = len(nums)
        # brute force time complexity = o(n^2)
        # for i in range(N+1):
        #     flag= 0 
        #     for j in range (N):
        #         if nums[j]==i:
        #             flag=1
        #             break
        #     if flag==0:
        #         return i 
        # optimal solution is 
        expected_sum = N * (N + 1) // 2
        actual_sum=0
        for i in range(N):
            actual_sum += nums[i]

        return expected_sum - actual_sum

            

        """
        :type nums: List[int]
        :rtype: int
        """
        