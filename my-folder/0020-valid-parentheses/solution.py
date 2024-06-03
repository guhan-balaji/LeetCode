class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_brackets = ['(', '{', '[']
        
        for c in s:
            if c in opening_brackets:
                stack.append(c)
            else:
                if not stack:
                    return False 
                b = stack.pop()

                if b == '(' and c != ')' or \
                   b == '{' and c != '}' or \
                   b == '[' and c != ']':
                   return False

        return len(stack) == 0                    
