class Solution(object):
    def isValid(self, s):
        stack = []
        p_map = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        for c in s:
            if c in {'(', '[', '{'}:
                stack.append(c)
            else:
                if not stack:
                    return False
                    
                p = stack.pop()
                if p_map[p] != c:
                    return False
        
        return len(stack) == 0
        """
        :type s: str
        :rtype: bool
        """
        
