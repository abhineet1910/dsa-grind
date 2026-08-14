class Solution(object):
    def findKthPositive(self, arr, k):
        n = len(arr)
        low = 0
        high = n-1
        while low<=high:
            mid = (low+high)//2
            if (arr[mid]-mid-1)<k:
                low = mid+1
            else:
                high = mid -1
        return low + k
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        