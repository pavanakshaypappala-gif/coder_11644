class Solution(object):
    def xorOperation(self, n, start):
        ans = start
        for i in range(1,n):
            ans=ans ^(start+2 * i)
        
        return ans
        