class Solution(object):
    def generate(self, numRows):
        # brute force be 
        # def ncr(n,r):
        #     result = 1
        #     for i in range(r):
        #         result = result*(n-i)
        #         result = result/(i+ 1)
        #     return result

        # ans =[]
        # for i in range(1,numRows+1):
        #     templist=[]
        #     for j in range(1,i):
        #         templist.append(ncr(i-1,j-1))
        #     templist.append(1)

        #     ans.append(templist)

        
        # return ans
        # optimal solution
        result =[[1]]
        for i in range(1,numRows):
            value = 1
            arr = [1]
            
            for j in range(i):
                value = value*(i-j)
                value = value // (j+1)
                arr.append(value)
            result.append(arr)
        return result

            

        
 
        