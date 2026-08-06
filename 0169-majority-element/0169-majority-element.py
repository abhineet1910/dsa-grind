class Solution(object):
    def majorityElement(self, nums):
        count = {}
        result = 0
        maxcount = 0
        for n in nums:
            count[n] = 1 + count.get(n,0)
            if count[n]>maxcount:
                result = n
            maxcount = max(count[n],maxcount)
        return result 
        """
        :type nums: List[int]
        :rtype: int
        """
        