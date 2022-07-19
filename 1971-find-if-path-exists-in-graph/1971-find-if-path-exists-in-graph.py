class Solution:
    def validPath(self, N: int, edges: List[List[int]], source: int, destination: int) -> bool:
        al=[]
        for i in range(N):
            al.append([])
        for i in edges:
            n,m=i[0],i[1]
            al[n].append(m)
            al[m].append(n)
        dist=[float('inf')]*N
        queue=[]  
        
        dist[source]=0
        queue.append(source)
        
        while queue:
            node=queue.pop(0)
            
            for i in al[node]:
                if dist[node]+1<dist[i]:
                    dist[i]=dist[node]+1
                    queue.append(i)
        if dist[destination]==float('inf'):
            return False
        return True