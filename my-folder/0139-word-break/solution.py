class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def wb(s: str) -> bool:
            if s == '':
                return True

            for word in wordDict:
                if s.startswith(word) and wb(s[len(word):]):
                    return True

            return False
        
        return wb(s)
