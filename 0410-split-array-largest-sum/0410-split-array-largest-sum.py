class Solution(object):
    def splitArray(self, nums, k):
        n = len(nums)
        def countsubarray(array,maxsum):
            subarray = 1 
            current_sum = 0
            for num in array:
                if current_sum + num <= maxsum:
                    current_sum += num
                else:
                    subarray += 1
                    current_sum = 0 
                    current_sum += num
            return subarray
        low = max(nums)
        high = sum(nums)
        while low<=high:
            mid = (low+high)//2
            groups = countsubarray(nums,mid)
            if groups<=k:
                answer = mid 
                high = mid-1
            else:
                low = mid +1
        return answer
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        