#Added a path array to the Dijkstra Algorithm

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        d=defaultdict(list)
        for i in roads:
            a,b,w=i
            d[a].append([b,w])
            d[b].append([a,w])
            
        pq=[]
        heapq.heapify(pq)
        
        dist=[float('inf')]*n
        ways=[0]*n # to check/count the ways of minimum traversal 
        
        dist[0]=0
        ways[0]=1
        heapq.heappush(pq,[0,0])
        
        while pq:
            node=heapq.heappop(pq)
            dis=node[0]
            prev=node[1]
            
            if dist[prev]<dis: continue #saves time reduces time complexity
            
            for i in d[prev]:
                nxt=i[0]
                nxtdis=i[1]
                if dist[nxt]>dis+nxtdis:
                    dist[nxt]=dist[prev]+nxtdis
                    ways[nxt]=ways[prev] # since this is the minimum path ways for current node is equal to the no of ways of the previous node 
                    heapq.heappush(pq,[dist[nxt],nxt])
                    
                elif dist[nxt]==dis+nxtdis: #if both the distance are equal,then you can traverse in both paths, thus adding both of them to no of paths.
                    ways[nxt]=(ways[nxt]+ways[prev])%1000000007
        
        return ways[n-1]
    
# We use Dijkstra algorithm to find the Shortest Path from src = 0 to dst = n - 1.
# While dijkstra, we create additional ways array, where ways[i] keeps the number of shortest path from src = 0 to dst = i. Then the answer is ways[n-1].