class Solution:
    def minimumTotal(self,a: List[List[int]]) -> int:
        n=len(a)
        dp=[[0]*n for _ in range(n)]
        for i in range(n):
            dp[n-1][i]=a[n-1][i]
        
        for i in range(n-2,-1,-1):
            for j in range(i,-1,-1):
                dp[i][j]=min(a[i][j]+dp[i+1][j],a[i][j]+dp[i+1][j+1])
        return dp[0][0]