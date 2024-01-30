class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        for c in set(s):
            if s.count(c) != t.count(c):
                return False
        return True
        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
