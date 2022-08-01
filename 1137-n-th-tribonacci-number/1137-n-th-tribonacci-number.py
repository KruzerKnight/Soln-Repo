class Solution:
    def tribonacci(self, n: int) -> int:
        if(n==0):
            return 0
        a=0
        b=0
        c=1
        for _ in range(n-1):
            a,b,c=b,c,a+b+c
        return c