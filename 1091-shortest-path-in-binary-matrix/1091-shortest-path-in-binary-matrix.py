class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        n=len(grid)
        
        directions=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        
        if grid[0][0]==0:
            q=[[1,0,0]]
        else:
            q=[]
        vis=set()
        
        while q:
            d,x,y=q.pop(0)
            if [x,y]==[n-1,n-1]:
                return d
            for i,j in directions:
                a,b=x+i,y+j
                
                if 0<=a<n and 0<=b<n and (a,b) not in vis and grid[a][b]==0:
                    vis.add((a,b))
                    q.append([d+1,a,b])
        return -1