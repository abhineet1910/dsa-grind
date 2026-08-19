class Solution(object):
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        #  this is the brute force i am able to do it 
        # take a time complexity of O(N*log 2 M )

        # def bs(array, t):
        #     low = 0 
        #     high = len(array)-1
        #     while low<=high:
        #         mid= (low+high)//2
        #         if array[mid]==t:
        #             return True
        #         elif array[mid]<t:
        #             low = mid+1
        #         else:
        #             high = mid - 1
        #     return False
        
        # for i in range(n):
        #     if matrix[i][0] <=target and target<=matrix[i][m-1]:
        #         if bs(matrix[i], target):
        #             return True

        # return False
        #  OPTIMAL SOLUTION IS TO SEARCH BINARY 
        row = 0
        col = m-1
        while row < n and col>=0:
            if matrix[row][col]==target:
                return True 
            elif matrix[row][col]>target:
                col -= 1
            else :
                row += 1
        return False

        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        