class Solution:
    def longestPalindrome(self, s: str) -> int:
        word_count = Counter(s)
        first_odd = True
        result = 0
        for (_, v) in word_count.items():
            if v % 2 == 0:
                result += v
            elif first_odd:
                result += v
                first_odd = False
            else:
                result += v - 1
        
        return result
