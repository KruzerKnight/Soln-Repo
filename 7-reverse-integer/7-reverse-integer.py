class Solution:
    def reverse(self, x: int) -> int:
        mini=-2**31
        maxi=2**31-1
        if x<0:
            s=str(x)
            s=s[0]+s[:0:-1]
        else:
            s=str(x)
            s=s[::-1]
        c=int(s)
        if c<mini or c>maxi:
            return 0
        return c