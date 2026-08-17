class Solution(object):
    def shipWithinDays(self, weights, days):
        n = len(weights)
        def daysrequired(wt,capacity):
            day = 1
            load = 0
            for i in range(0,len(weights)):
                if (load+wt[i])>capacity:
                    day = day+1
                    load = wt[i]
                else:
                    load += wt[i]
            return day

        low = max(weights)
        high = sum(weights)
        while low<=high:
            mid = (low+high)//2
            days_need=daysrequired(weights,mid)
            if days_need <= days:
                high = mid-1
            else:
                low = mid +1
        return low 



        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        