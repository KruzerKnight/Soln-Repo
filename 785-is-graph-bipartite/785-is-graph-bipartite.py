class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def Bipartite(i):
            q=[]
            q.append(i)
            color[i]=1
            
            while q:
                node=q.pop(0)
                
                for j in graph[node]:
                    if color[j]==-1:
                        color[j]=1-color[node] #coloring the graph in diff colors
                        q.append(j)
                    elif color[j]==color[node]:
                        return False
            return True
        
        n=len(graph)
        color=[-1]*n
        
        for i in range(n):
            if color[i]==-1:
                if not Bipartite(i):
                    return False
        return True