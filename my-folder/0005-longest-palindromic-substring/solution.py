class Solution:
    def longestPalindrome(self, s: str) -> str:
        def get_longest(s: str, l: int, r:int):
            palindrome = s[l]
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindrome = s[l: r+1]
                l -= 1
                r += 1
            return palindrome
                


        longest = ''
        for i in range(len(s)):
            o = odd_length_palindrome = get_longest(s, i, i)
            e = even_length_palindrome = get_longest(s, i, i + 1)

            if len(o) > len(longest):
                longest = o
            
            if len(e) > len(longest):
                longest = e

        return longest
