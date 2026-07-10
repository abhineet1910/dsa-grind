class Solution(object):
    def fib(self, n):
        if (n<=1):
            return n
        first = self.fib(n - 1)
        last = self.fib(n - 2)
        return first + last
        """
        :type n: int
        :rtype: int
        """
        