class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n=len(heights)
        m=len(heights[0])
        
        directions=[(0,-1),(0,1),(1,0),(-1,0)]
        
        pvis=[[0]*m for _ in range(n)]
        avis=[[0]*m for _ in range(n)]
        res=[]
        
        # two visited lists for both oceans
        
        def dfs(x,y,vis):
                        
            vis[x][y]=1
            
            for d in directions:
                i,j=x+d[0],y+d[1]
                
                #dfs is called only if the vertices are within the limit
                
                if i<0 or i>=n or j<0 or j>=m or heights[i][j]<heights[x][y] or vis[i][j]:
                    continue
                dfs(i,j,vis)
                
        #accsess the peaks starting from the boundaries
        
        for i in range(n):
            dfs(i,0,pvis)
            dfs(i,m-1,avis)
            
        for j in range(m):
            dfs(0,j,pvis)
            dfs(n-1,j,avis)
            
        #if both visited array have as 1 then the water from the point can go to both the oceans
            
        for i in range(n):
            for j in range(m):
                if pvis[i][j] and avis[i][j]:
                    res.append([i,j])
        
        
        return res