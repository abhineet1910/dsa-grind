class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        ans=set()
        # This is the brute force approch 
        # for i in range(n):
        #     for j in range (i+1,n):
        #         for k in range(j+1,n):
        #             if nums[i]+nums[j]+nums[k] == 0:
        #                 triplet = [nums[i],nums[j],nums[k]]
        #                 triplet.sort()
        #                 triplet = tuple(triplet)
        #                 ans.add(triplet)



        # this is the better solution
        for i in range(n):
            seen = set()
            for j in range(i+1,n):
                target=-(nums[i]+nums[j])
                if target in seen:
                    triplet=[nums[i],nums[j],target]
                    triplet.sort()
                    

                    ans.add(tuple(triplet))
                seen.add(nums[j])
                

        return [list(triplet) for triplet in ans]

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        