class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
                     
        n=len(bombs)
        res=0
        d=defaultdict(list)
        
        for i in range(n):
            for j in range(n):
                #checking whether the bomb is in range of the other bomb
                if i!=j and bombs[i][2]**2>=(bombs[i][0]-bombs[j][0])**2 + (bombs[i][1]-bombs[j][1])**2:
                    d[i]+=[j]
        
        def dfs(i,vis):
            for bomb in d[i]:
                if bomb not in vis:
                    vis.append(bomb)
                    dfs(bomb,vis)
            return
        
        
        for i in range(n):
            vis=[i]
            dfs(i,vis)
            res=max(res,len(vis))
            
        return res