from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s1 = Counter(ransomNote)
        s2 = Counter(magazine)

        for keys,values in s1.items():
            if s2[keys]<values:
                return False
        else:
            return True
        