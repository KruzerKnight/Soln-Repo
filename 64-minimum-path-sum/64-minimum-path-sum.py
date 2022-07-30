class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        
        #memoization
        
        dp=[[-1]*m for _ in range(n)]
        # #print(n,m,dp)
        # def fun(i,j):
        #     #print(i,j,grid[i][j])
        #     if i==0 and j==0:
        #         return grid[0][0]
        #     if i<0 or j<0:
        #         return float('inf')
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     dp[i][j]=grid[i][j]+min(fun(i-1,j),fun(i,j-1))
        #     return dp[i][j]
        # return fun(n-1,m-1)
        
        #tabulation
        for i in range(n):
            for j in range(m):
                
                if i==0 and j==0:
                    dp[i][j]=grid[i][j]
                else:
                    up=float('inf')
                    left=float("inf")
                    if i>0:
                        up=dp[i-1][j]
                    if j>0:
                        left=dp[i][j-1]
                    dp[i][j]=grid[i][j]+min(up,left)
                #print(i,j,dp[i][j])
        return dp[n-1][m-1]