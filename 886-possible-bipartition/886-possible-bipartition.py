class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
            
        al=defaultdict(list)
        for a,b in dislikes:
            al[a].append(b)
            al[b].append(a)
        
        
        
        def Bipartite(i):
            q=[]
            q.append(i)
            color[i]=1
            
            while q:
                node=q.pop(0)
                
                for j in al[node]:
                    if color[j]==-1:
                        color[j]=1-color[node] #coloring the graph in diff colors
                        q.append(j)
                    elif color[j]==color[node]:
                        return False
            return True
        
        
        color=[-1]*(n+1)
        
        for i in range(n):
            if color[i]==-1:
                if not Bipartite(i):
                    return False
        return True