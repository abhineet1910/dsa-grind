class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        words.reverse()
        result = " ".join(words)
        return result
        """
        :type s: str
        :rtype: str
        """
        