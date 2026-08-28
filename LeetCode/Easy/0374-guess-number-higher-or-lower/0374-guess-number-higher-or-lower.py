# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        first = 1
        last = n
        while first<=last:
            mid = (first+last)//2
            pick = guess(mid)
            if pick == 0:
                return mid
            elif pick == -1:
                last = mid -1
            else:
                first = mid+1
        return 0
        