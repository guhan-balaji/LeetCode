class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        else:
            sub_string = dict({})
            max_len = 1
            l_idx = 0

            for r_idx, c in enumerate(s):
                sub_string[c] = sub_string[c] + 1 if c in sub_string else 1
                while sub_string[c] > 1:
                    sub_string[s[l_idx]] -= 1
                    l_idx += 1
                max_len = max(max_len, (r_idx - l_idx) + 1)
            
            return max_len
        
