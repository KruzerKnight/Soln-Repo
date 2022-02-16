class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            s=str(x)
            s=s[0]+s[:0:-1]
        else:
            s=str(x)
            s=s[::-1]
        c=int(s)
        if c<-2**31 or c>2**31-1:
            return 0
        return c