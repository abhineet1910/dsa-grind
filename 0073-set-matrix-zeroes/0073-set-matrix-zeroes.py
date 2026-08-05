class Solution(object):
    def setZeroes(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        # optimal approch
        col0=1
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    if j != 0:
                        matrix[0][j]=0
                    else:
                        col0=0
        for i in range(1,n):
            for j in range(1,m):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j] = 0
        if matrix[0][0]==0:
            for j in range(m):
                matrix[0][j]=0
        if col0==0:
            for i in range(n):
                matrix[i][0]=0
        
        # better approch 
        # col = [0]*m
        # row = [0]*n
        # for i in range(n):
        #     for j in range(m):
        #         if matrix[i][j]==0:
        #             row[i]=1
        #             col[j]=1

        # for i in range(n):
        #     for j in range(m):
        #         if row[i] or col[j]:
        #             matrix[i][j]=0
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
        