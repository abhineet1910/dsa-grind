class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # this is the extream brute force i thing it as 
        # ansarray = []
        # for num in nums1:
        #     ansarray.append(num)
        # for num in nums2:
        #     ansarray.append(num)
        # ansarray.sort()
        # n = len(ansarray)
        # if n % 2 == 1:
        #     return ansarray[n // 2]
        # else:
        #     middle1 = ansarray[n // 2 - 1]
        #     middle2 = ansarray[n // 2]
        #     return (middle1 + middle2) / 2.0

        # this is gonna take tc or O(n*2) ans sc of O(n)
        
        # better solution is the two pointer approch 
        # n1 = len(nums1)
        # n2 = len(nums2)
        # total = n1 + n2

        # pointer1=0
        # pointer2=0

        # previous = 0
        # current = 0

        # for i in range(total//2+1):
        #     previous = current 

        #     if pointer1 < n1 and pointer2 < n2:

        #         if nums1[pointer1] <= nums2[pointer2]:
        #             current = nums1[pointer1]
        #             pointer1 += 1

        #         else:
        #             current = nums2[pointer2]
        #             pointer2 += 1

        #     elif pointer1 < n1:

        #         current = nums1[pointer1]
        #         pointer1 += 1

        #     else:

        #         current = nums2[pointer2]
        #         pointer2 += 1
        # if total%2 == 0:
        #     return (previous + current) /2.0
        # else:
        #     return current

        # time complexity of O((n + m) / 2) → O(n + m)
        # Space Complexity: O(1)

        # use of binary search let get to the optimal solution
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2
        leftsize = (total + 1) // 2

        low, high = 0, n1

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = leftsize - cut1

            l1 = nums1[cut1 - 1] if cut1 > 0 else float("-inf")
            r1 = nums1[cut1] if cut1 < n1 else float("inf")
            l2 = nums2[cut2 - 1] if cut2 > 0 else float("-inf")
            r2 = nums2[cut2] if cut2 < n2 else float("inf")

            if l1 <= r2 and l2 <= r1:
                if total % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                else:
                    return max(l1, l2)
            elif l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1

        raise ValueError("Input arrays are not sorted")
        
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        