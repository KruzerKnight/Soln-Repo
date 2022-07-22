class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n=len(land)
        m=len(land[0])
        
        l=[]
        
        vis=[[0]*m for _ in range(n)]
        mix=[n,m,0,0]
        
        def dfs(i,j):
            flag=True
                       
            
            if i<0 or i>=n or j<0 or j>=m or land[i][j]==0 or vis[i][j]:
                return 
            
            vis[i][j]=1
            
            mix[0]=min(mix[0],i)
            mix[1]=min(mix[1],j)
            mix[2]=max(mix[2],i)
            mix[3]=max(mix[3],j)
            
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
            
        
        for i in range(n):
            for j in range(m):
                if land[i][j]==1 and not vis[i][j]:
                    mix=[n,m,0,0]
                    dfs(i,j)
                    l.append(mix)
                    
        
        return l