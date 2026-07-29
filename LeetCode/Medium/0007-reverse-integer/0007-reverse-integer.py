class Solution(object):
    def reverse(self, x):
        temp=abs(x)
        r =0 
        while temp>0:
            r = r *10 + temp%10
            temp = temp//10
        if r > (2**31 -1) or r<-(2**31):
            return 0
        else:
            if x>0:
                return r
            else:
                return -r

        
        
        