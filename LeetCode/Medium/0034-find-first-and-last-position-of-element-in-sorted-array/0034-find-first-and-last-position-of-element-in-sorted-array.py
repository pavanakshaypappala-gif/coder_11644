class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0 
        right = len(nums)-1
        first = -1
        while(left<=right):
            mid = (left+right)//2
            if nums[mid] == target:
                first = mid
                right = mid -1
            elif nums[mid]>=target:
                right = mid -1
            else:
                left = mid+1
        left = 0 
        right = len(nums)-1
        lst = -1
        while(left<=right):
            mid = (left+right)//2
            if nums[mid] == target:
                lst = mid
                left = mid +1
            elif nums[mid]>=target:
                right = mid -1
            else:
                left = mid+1
        return [first,lst]
        