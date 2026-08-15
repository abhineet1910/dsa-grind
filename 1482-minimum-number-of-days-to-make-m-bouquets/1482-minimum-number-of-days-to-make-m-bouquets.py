class Solution(object):
    def minDays(self, bloomDay, m, k):
        n = len(bloomDay)
        #  this is the extream brute force with tc of O(maxi-mini+1)*O(n)-to check possible of not O(maxi-mini+1) this is the main loop
        def possible(arr,day,m,k,n):
            cnt = 0
            no_of_bouquet = 0
            for i in range(n):
                if arr[i]<=day:
                    cnt += 1
                else:
                    no_of_bouquet += cnt/k
                    cnt = 0 
            no_of_bouquet += cnt/k
            if no_of_bouquet>=m:
                return True
            else:
                return False
        # minimum = min(bloomDay)
        # maximum = max(bloomDay)
        # for i in range(minimum,maximum+1):
        #     if possible(bloomDay,i,m,k,n) == True:
        #         return i
        # return -1
        # 

        # the optimal solution is binary search and that is 
        if (m*k)>n:
            return -1
        low = min(bloomDay)
        high = max(bloomDay)
        while low<=high:
            mid = (low + high)//2
            if possible(bloomDay,mid,m,k,n) == True:
                high = mid-1
                
            else:
                low = mid+1
        return low
        

                





        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """
        