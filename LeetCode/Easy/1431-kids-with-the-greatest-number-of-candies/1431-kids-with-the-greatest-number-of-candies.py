class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c = max(candies)
        result = []
        for c in candies:
            if c+extraCandies >= max_c:
                result.append(True)
            else:
                result.append(False)
        return result