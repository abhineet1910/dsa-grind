# You are given a 3-digit number n, Find whether it is an Armstrong number or not.
#
# An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. 371 is an Armstrong number since 33 + 73 + 13 = 371.
#
# Examples:
#
# Input: n = 153
# Output: true
# Explanation: 153 is an Armstrong number since 13 + 53 + 33 = 153.
# Input: n = 372
# Output: false
# Explanation: 372 is not an Armstrong number since 33 + 73 + 23 = 378.



class Solution:
    def armstrongNumber(self, n):
        # code here
        x = n
        sum = 0
        if x < 0:
            return False
        else:
            while x > 0:
                ld = x % 10
                sum = sum + (ld * ld * ld)
                x = x // 10
            if n == sum:
                return True
            else:
                return False

