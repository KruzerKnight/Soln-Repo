class Solution:
    def climbStairs(self, n: int) -> int:
        s=0
        s1=1
        for i in range(n):
            s,s1=s1,s+s1
        return(s1)