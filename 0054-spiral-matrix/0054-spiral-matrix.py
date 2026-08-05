class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []

        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1

        ans = []

        while top <= bottom and left <= right:

            # Traverse Top Row
            for col in range(left, right + 1):
                ans.append(matrix[top][col])
            top += 1

            # Traverse Right Column
            for row in range(top, bottom + 1):
                ans.append(matrix[row][right])
            right -= 1

            # Traverse Bottom Row (if it exists)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    ans.append(matrix[bottom][col])
                bottom -= 1

            # Traverse Left Column (if it exists)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    ans.append(matrix[row][left])
                left += 1

        return ans


        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        