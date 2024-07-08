class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rn_c = Counter(ransomNote)
        m_c = Counter(magazine)

        for k, v in rn_c.items():
            if k not in m_c or v > m_c[k]:
                return False
        
        return True
