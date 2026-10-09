class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        prefix = [0]*len(nums)
        prefix[0]=nums[0]
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]+nums[i]
        r = []
        for i in range(len(nums)):
            ls = prefix[i]-nums[i]
            rs = prefix[-1]-(prefix[i])
            r.append(abs(ls-rs))
 
        return r