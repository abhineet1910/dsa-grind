class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        # ans=set()
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
        # for i in range(n):
        #     seen = set()
        #     for j in range(i+1,n):
        #         target=-(nums[i]+nums[j])
        #         if target in seen:
        #             triplet=[nums[i],nums[j],target]
        #             triplet.sort()
                    

        #             ans.add(tuple(triplet))
        #         seen.add(nums[j])


        # return [list(triplet) for triplet in ans]



        #  for most optimal solution with space complexity = o(no of triplets )
        ans = []
        nums.sort()
        for i in range(n):
            if i != 0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j<k:
                total_sum = nums[i]+nums[j]+nums[k]
                if total_sum <0:
                    j += 1
                elif total_sum > 0:
                    k -=1
                else:
                    ans.append([nums[i], nums[j], nums[k]])

                    # Skip duplicates
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1

                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    # Move both pointers
                    j += 1
                    k -= 1
        return ans 
                

            

        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        