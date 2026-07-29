class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i,num in enumerate(nums):
            sub = target - num

            if sub in dict:
                return[i,dict[sub]]

            dict[num] = i

    

        

        