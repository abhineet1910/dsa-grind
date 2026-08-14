class Solution(object):
    def minEatingSpeed(self, piles, h):
        #  this is the extream brute force that happens 
        # max_speed = max(piles)
        # for speed in range(1, max_speed + 1):

        #     total_hours = 0
        #     for pile in piles:
        #         hours = (pile + speed - 1) // speed
        #         total_hours += hours
        #     if total_hours<=h:
        #         return speed


        # the optimal solution 
        #  first low ptr is min valye 
        #  nst high ptr is the max(pile )
        def caneatbanana(p,h,speed):
            total_hours = 0 
            for pile in p:
                hours = (pile + speed - 1) // speed
                total_hours += hours
            if total_hours<=h:
                return True
            else:
                return False
        low = 1
        high = max(piles)
        while low<high:
            mid = (low + high)//2
            if caneatbanana(piles,h,mid):
                high = mid
            else:
                low = mid+1
        return low 

        
                
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        