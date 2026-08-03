class Solution(object):
    def rearrangeArray(self, nums):
        # brute force this take 
        # this gonna takes tc of O(2N) AND SC OF O(N)
        # pos = []
        # neg = []
        n = len(nums)
        # for i in range(n):
        #     if nums[i]>0:
        #         pos.append(nums[i])
        #     else:
        #         neg.append(nums[i])
        # for i in range(n/2):
        #     nums[i*2]=pos[i]
        #     nums[i*2+1]=neg[i]
        # return nums
        # optimal approch 
        ans = [0]*n
        posindex=0
        negindex=1
        for i in range(n):
            if nums[i]>0:
                ans[posindex] = nums[i]
                posindex += 2
            else:
                ans[negindex]=nums[i]
                negindex+=2
        return ans


        """
        :type nums: List[int]
        :rtype: List[int]
        """
        