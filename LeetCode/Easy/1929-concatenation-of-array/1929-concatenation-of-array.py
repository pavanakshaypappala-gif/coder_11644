class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        c = []
        for num in nums:
            c.append(num)
        for num in nums:
            c.append(num)
        return c
        