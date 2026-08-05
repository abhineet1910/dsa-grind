class Solution(object):
    def setZeroes(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        col = [0] * m
        row = [0] * n
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1

        for i in range(n):
            for j in range(m):
                if row[i] or col[j]:
                    matrix[i][j] = 0
        # lets dive brute force 
        # def markRow(i):
        # for j in range(m):
        #     if matrix[i][j] != 0:
        #         matrix[i][j] = -1 
        # def markcol(j):
        #     for i in range(m):
        #         if matrix[i][j] != 0:
        #             matrix[i][j] = -1 

        # for i in range(n):
        #     for j in range(m):
        #         if matrix[i][j] == 0:
        #             markrow(i)
        #             markcol(j)
        # for i in range(n):
        #     for j in range(m):
        #         if matrix[i][j] == -1:
        #             matrix[i][j] = 0
        return matrix




        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        