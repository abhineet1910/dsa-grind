class Solution(object):
    def longestConsecutive(self, nums):
        # this is the brute force i applied 
        # if not nums:
        #     return 0
        # nums.sort()

        # current_len = 1
        # max_len = 1

        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1] + 1:
        #         current_len += 1
        #     elif nums[i] == nums[i - 1]:
        #         continue
        #     else:
        #         max_len = max(max_len, current_len)
        #         current_len = 1

        # max_len = max(max_len, current_len)
        #  this is the optimal approch 
        num_set = set(nums)
        max_len = 0
        for num in num_set:
            if(num-1) not in num_set:
                current = num
                lenght = 1
                while (current+1) in num_set:
                    current = current+1
                    lenght = lenght + 1
                max_len = max(max_len,lenght)


        return max_len

        
        

        """
        :type nums: List[int]
        :rtype: int
        """
        