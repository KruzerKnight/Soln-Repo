class Solution:
    def validPath(self, N: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        
        #making an adjacency list from given edges
        al=[]
        for i in range(N):
            al.append([])
        for i in edges:
            n,m=i[0],i[1]
            al[n].append(m)
            al[m].append(n)
            
#         #a list for saving distance of the nodes from each other
#         dist=[float('inf')]*N
#         queue=[]  
        
#         dist[source]=0
#         queue.append(source)
        
#         #using shortest path to all nodes from source, thus if a node doesnt have any distance from source then it is not connected thats why using the shortest distance technique
        
#         while queue:
#             node=queue.pop(0)
            
#             for i in al[node]:
#                 if dist[node]+1<dist[i]:
#                     dist[i]=dist[node]+1
#                     queue.append(i)
#         if dist[destination]==float('inf'):
#             return False
#         return True


#Trying Simple BFS

        queue=[]
        vis=[0]*N
        vis[source]=1
        queue.append(source)
        while queue:
            node=queue.pop(0)
            if node==destination:
                return True
            for i in al[node]:
                if not vis[i]:
                    queue.append(i)
                    vis[i]=1
        return False