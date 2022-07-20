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
        ways=[0]*n
        
        dist[0]=0
        ways[0]=1
        heapq.heappush(pq,[0,0])
        
        while pq:
            node=heapq.heappop(pq)
            dis=node[0]
            prev=node[1]
            
            for i in d[prev]:
                nxt=i[0]
                nxtdis=i[1]
                if dist[nxt]>dis+nxtdis:
                    dist[nxt]=dist[prev]+nxtdis
                    ways[nxt]=ways[prev]
                    heapq.heappush(pq,[dist[nxt],nxt])
                    
                elif dist[nxt]==dis+nxtdis:
                    ways[nxt]=(ways[nxt]+ways[prev])%1000000007
        
        return ways[n-1]