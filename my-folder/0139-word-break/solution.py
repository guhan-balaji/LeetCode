class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        @cache
        def word_break(s: str) -> bool:
            if s == '':
                return True

            # if s in memo:
            #     return memo[s]

            for word in wordDict:
                if s.startswith(word):
                    if word_break(s[len(word):]):
                        return True
            
            return False

        return word_break(s)
