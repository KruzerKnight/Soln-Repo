class Solution:
    def arrangeCoins(self, n: int) -> int:
        count=0
        if n<=2:
            return 1
        for i in range(1,n):
            count+=i
            if count==n:
                return i
            if count>n:
                return i-1