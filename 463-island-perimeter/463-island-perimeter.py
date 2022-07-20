class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        p=0
        
        for i in range(n):
            for j in range(m):
                
                p+=4*grid[i][j]
                if i>0 : p-=grid[i][j]*grid[i-1][j]
                if i<n-1 : p-=grid[i][j]*grid[i+1][j]
                if j>0 : p-=grid[i][j]*grid[i][j-1]
                if j<m-1 : p-=grid[i][j]*grid[i][j+1]
        
        return p