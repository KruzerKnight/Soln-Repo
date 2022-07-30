class Solution:
    def uniquePathsWithObstacles(self, dps: List[List[int]]) -> int:
        m=len(dps)
        n=len(dps[0])
        dp=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if dps[i][j]==1:
                    dp[i][j]=0
                elif i==0 and j==0:
                    dp[i][j]=1
                else:
                    up=0
                    down=0
                    if i>=1:
                        up=dp[i-1][j]
                    if j>=1:
                        down=dp[i][j-1]
                    dp[i][j]=up+down
        #print(dp)
        return dp[m-1][n-1]