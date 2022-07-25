class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        m=len(mat)
        n=len(mat[0])
        dirs=[[0,1], [1,0], [-1,0], [0,-1]]
        q=[]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append([i,j])
        
        vis=set()
        while q:
            node=q.pop(0)
            for d in dirs:
                x,y=node[0]+d[0],node[1]+d[1]
                if 0<=x<m and 0<=y<n and (x,y) not in vis and mat[x][y]==1:
                    mat[x][y]=1+mat[node[0]][node[1]]
                    q.append([x,y])
                    vis.add((x,y))
            #print(q)
        return mat