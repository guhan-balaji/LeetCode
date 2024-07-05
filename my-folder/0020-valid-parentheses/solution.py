class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for ch in s:
            if ch in ['(', '[', '{']:
                stk.append(ch)
            elif not stk:
                return False
            else:
                last = stk.pop()
                if last == '(' and ch != ')' or \
                   last == '[' and ch != ']' or \
                   last == '{' and ch != '}':
                   return False
        
        return len(stk) == 0
                
