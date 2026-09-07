class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        temp_nums2 = list(nums2) 
        
        for val in nums1:
            if val in temp_nums2:
                result.append(val)
                temp_nums2.remove(val)
                
        return result