class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        start = 0
        c_set = set()

        for c in s:
            if c not in c_set:
                c_set.add(c)
                longest = max(longest, len(c_set))
            else:
                while s[start] != c:
                    c_set.remove(s[start])
                    start += 1
                start += 1
        
        return longest
