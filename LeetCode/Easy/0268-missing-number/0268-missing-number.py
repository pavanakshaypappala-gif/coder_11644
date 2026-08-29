class Solution(object):
    def missingNumber(self, nums):
        add = sum(nums)
        exp = sum(range(len(nums)+1))
        return exp - add     
        