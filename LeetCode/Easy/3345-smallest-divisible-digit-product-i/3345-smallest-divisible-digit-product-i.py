class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while n<101:
            x = n
            pro = 1
            while x >0:
                pro *= x%10
                x //=10
            if pro % t == 0:
                return n
        
            n=n+1
        