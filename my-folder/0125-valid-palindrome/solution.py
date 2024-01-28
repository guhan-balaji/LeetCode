class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())

        return s[::-1] == s
        """
        :type s: str
        :rtype: bool
        """
        
