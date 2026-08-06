class Solution(object):
    def majorityElement(self, nums):
        # better approch for this 
        # count = {}
        # result = 0
        # maxcount = 0
        # for n in nums:
        #     count[n] = 1 + count.get(n,0)
        #     if count[n]>maxcount:
        #         result = n
        #     maxcount = max(count[n],maxcount)
        candidate = None
        count = 0

        for num in nums:

            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate
        
        """
        :type nums: List[int]
        :rtype: int
        """
        