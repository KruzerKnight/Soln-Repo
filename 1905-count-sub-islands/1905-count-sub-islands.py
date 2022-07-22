class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n=len(grid2)
        m=len(grid2[0])
        
        vis=[[0]*m for _ in range(n)]
        count=0
        
        def dfs(i,j):
            flag=True
                       
            
            if i<0 or i>=n or j<0 or j>=m or grid2[i][j]==0 or vis[i][j]:
                return flag
            
            flag=flag and grid1[i][j]==1
            vis[i][j]=1
            
            #print(i,j,flag)
            
            flag=dfs(i-1,j) and flag
            flag=dfs(i+1,j) and flag
            flag= dfs(i,j-1) and flag
            flag=dfs(i,j+1) and flag
            
            #print('here',flag)
            return flag
        
        for i in range(n):
            for j in range(m):
                if grid2[i][j]==1 and not vis[i][j]:
                    #print('hehe',i,j)
                    if dfs(i,j):
                        #print('helo',i,j)
                        count+=1
        
        return count