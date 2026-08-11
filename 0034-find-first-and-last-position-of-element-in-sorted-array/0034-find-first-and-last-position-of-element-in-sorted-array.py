class Solution(object):
    def searchRange(self, nums, target):

        n = len(nums)

        lb = -1
        hb = -1

        # Find first occurrence
        low = 0
        high = n - 1

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] == target:
                lb = mid
                high = mid - 1

            elif nums[mid] > target:
                high = mid - 1

            else:
                low = mid + 1

        # Find last occurrence
        low = 0
        high = n - 1

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] == target:
                hb = mid
                low = mid + 1

            elif nums[mid] > target:
                high = mid - 1

            else:
                low = mid + 1

        return [lb, hb]