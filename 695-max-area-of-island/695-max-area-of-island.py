class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        
        vis=[[0]*m for _ in range(n)]
        maxi=0
        
        def dfs(i,j):
            
            if i<0 or i>=n or j<0 or j>=m or grid[i][j]==0 or vis[i][j]:
                return 0
            
            vis[i][j]=1
            return 1+dfs(i-1,j)+dfs(i+1,j)+dfs(i,j-1)+dfs(i,j+1)
            
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] and not vis[i][j]:
                    maxi=max(maxi,dfs(i,j))
        
        return maxi