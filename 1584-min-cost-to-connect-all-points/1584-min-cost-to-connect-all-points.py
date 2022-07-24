class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        #using prims algorithm for minimum spanning tree
        # and the let the points be of their ind.no itself
        
        manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        
        n=len(points)
        d=defaultdict(list)
        
        for i in range(n):
            for j in range(i+1,n):
                
                dist=manhattan(points[i],points[j])
                d[i].append([dist,j])
                d[j].append([dist,i])
        
        count=1
        res=0
        visited=[0]*n
        pq=d[0]
        visited[0] = 1
        heapify(pq)
        while pq:
            dist,j=heappop(pq)
            if not visited[j]:
                visited[j]=1
                count+=1
                res+=dist
                for adj in d[j]:heappush(pq, adj)
            if count >= n: break        
        return res