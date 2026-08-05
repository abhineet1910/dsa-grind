class Solution(object):
    def subarraySum(self, nums, k):
        # optimal solution 
        prefix_sum = 0
        count = 0

        prefix_map = {0: 1}

        for num in nums:

            prefix_sum += num

            if prefix_sum - k in prefix_map:
                count += prefix_map[prefix_sum - k]

            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1

        return count
        # brute force 
       
        n = len(nums)
        cnt = 0

        for i in range(n):
            curr_sum = 0 
            for j in range(i, n):
                #  for better approch just use 

                curr_sum += nums[j]
                # curr_sum = 0

                # # Sum from i to j (inclusive)
                # for idx in range(i, j + 1):
                #     curr_sum += nums[idx]

                if curr_sum == k:
                    cnt += 1

        return cnt
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        