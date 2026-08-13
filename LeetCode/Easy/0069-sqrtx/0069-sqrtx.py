class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        j = x
        ans = -1
        while i<=j:
            mid = (i+j)//2
            sq = mid*mid
            if sq == x:
                return mid
            elif x < sq:
                j = mid - 1
            else:
                ans = mid
                i = mid+1
        return ans
        