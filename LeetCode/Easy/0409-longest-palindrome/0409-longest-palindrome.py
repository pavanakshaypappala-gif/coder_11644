class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq ={}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        count = 0 
        flag = 0
        for value in freq.values():
            count+=(value//2)*2
            if value%2==1:
                flag=1
        if flag:
            return count+1
        else:
            return count

        