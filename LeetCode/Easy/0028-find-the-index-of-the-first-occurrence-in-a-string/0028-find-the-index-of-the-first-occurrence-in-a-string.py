class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = haystack.strip()
        l = len(needle)
        for i in range(0,len(n)-l+1):
            if needle==n[i:i+l]:
                return i
        
        return -1