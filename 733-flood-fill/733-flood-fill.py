class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        n=len(image)
        m=len(image[0])
        src=image[sr][sc]
        
        def dfs(i,j):
            
            
            if i<0 or i>=n or j<0 or j>=m:
                return
            if image[i][j]!=src:
                return
            image[i][j]=color
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        if src==color:
            return image
                    
        dfs(sr,sc)
        return image