class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        longest = 0
        used_odd = False
        
        for v in counter.values():
            if v % 2 == 0:
                longest += v
            elif not used_odd:
                longest += v
                used_odd = True
            else:
                longest += v - 1
        
        return longest
