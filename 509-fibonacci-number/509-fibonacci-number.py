class Solution:
    def fib(self, num: int) -> int:
        l=[0]*(num+1)
        def kruz(n):
            if n==0:
                return 0
            if n==1 or n==2:
                return 1
            if l[n]!=0:
                return l[n]
            l[n]=kruz(n-1)+kruz(n-2)
            return l[n]
        return kruz(num)
    