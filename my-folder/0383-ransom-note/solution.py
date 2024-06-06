class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_counter = Counter(magazine)

        for c in ransomNote:
            if c not in m_counter or m_counter[c] < 1:
                return False
            else:
                m_counter[c] -= 1
            
        return True
