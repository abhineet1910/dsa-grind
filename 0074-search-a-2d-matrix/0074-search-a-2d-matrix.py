class Solution(object):
    def searchMatrix(self, matrix, target):
        # let be the brute force for this 
        n = len(matrix)
        m = len(matrix[0])
        # this si sthe extream brute force
        # for i in range(n):
        #     for j in range(m):
        #         if matrix[i][j]==target:
        #             return True 
        # return False
        # better approch 

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
        #         return bs(matrix[i],target)
        # return False

        # for optimal approch 
        low = 0
        high = (n*m)-1
        while low<=high:
            mid = (low+high)//2
            row= mid/m
            col=mid%m
            if matrix[row][col]==target:
                return True
            elif matrix[row][col] < target:
                low = mid+1
            else:
                high = mid - 1
        return False





        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        