class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        
        fresh=[0]
        rot=[]
        mint=0
                
        def bfs(i,j):
            
            if i<0 or i>=n or j<0 or j>=m or grid[i][j]==0 or grid[i][j]==2:
                return
            rot.append([i,j])
            fresh[0]-=1
            grid[i][j]=2
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    rot.append([i,j])
                elif grid[i][j]==1:
                    fresh[0]+=1
                    
        while fresh[0] and rot:
            limit=len(rot)
            for i in range(limit):
                s,r=rot.pop(0)
                bfs(s,r-1)
                bfs(s,r+1)
                bfs(s-1,r)
                bfs(s+1,r)
            mint+=1
        
        if fresh[0]:
            return -1
        return mint