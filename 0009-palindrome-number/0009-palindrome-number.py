class Solution(object):
    def isPalindrome(self, x):
        orignal = x
        reverse_no = 0
        if x<0:
            return False
        else:
            while x>0:
                
                ld = x % 10                  
                reverse_no = reverse_no * 10 + ld
                x = x // 10 
            if (orignal==reverse_no):
                return True
            else:
                return False
            
        """
        :type x: int
        :rtype: bool
        """
        