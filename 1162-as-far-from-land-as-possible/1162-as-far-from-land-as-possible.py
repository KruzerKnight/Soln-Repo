# https://assets.leetcode.com/users/abadawi/image_1566506498.png

# According to the pic the possible loops give the no maximum distance of nearest land to a water source
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        n=len(grid)
        m=len(grid[0])
        
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        q=[]
                
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    q.append((i,j,0))
        
        if len(q)==m*n or len(q)==0:
            return -1
        
        for x,y,d in q:
            for i,j in directions:

                X,Y=x+i,y+j  #adjacent cells boundaries

                if X<0 or X>=n or Y<0 or Y>=m or grid[X][Y]:
                    continue

                q.append((X,Y,d+1))
                grid[X][Y]=1
                    
        return q[-1][-1]
    