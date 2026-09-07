class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n,a,b = len(nums),sum(set(nums)),sum(nums)

        s = n*(n+1)//2
        return [b-a,s-a]