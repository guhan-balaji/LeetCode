class Solution:
    def longestPalindrome(self, s: str) -> int:
        c_count = Counter(s)
        
        result = 0
        is_first_odd_char = True

        for (_, v) in c_count.items():
            if v % 2 == 0:
                result += v
            else:
                result += v if is_first_odd_char else v - 1
                is_first_odd_char = False
        
        return result


