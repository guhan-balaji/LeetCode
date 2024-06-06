class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        substring = set()
        longest_length = length = 0
        l = 0

        for r, c in enumerate(s):
            if c not in substring:
                length +=1
                longest_length = max(longest_length, length)
                substring.add(c)
            else:
                while l <= r:
                    if s[l] != c:
                        substring.remove(s[l])
                        l += 1
                        length -= 1
                    else:
                        l += 1
                        break
        
        return longest_length
        
