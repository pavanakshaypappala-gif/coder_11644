class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 1
        for j in range(1,len(nums)):
            if nums[j]!=nums[i-1]:
                i+=1
                nums[i-1]=nums[j]
        return i
        