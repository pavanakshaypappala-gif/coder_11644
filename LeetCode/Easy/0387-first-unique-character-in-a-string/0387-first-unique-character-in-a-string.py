class Solution:
    def firstUniqChar(self, s: str) -> int:
        s1 = list(s)
        for i in range(len(s1)):
            ch=s[i]
            if s.count(ch)==1:
                return i
        else:
            return -1
                
        