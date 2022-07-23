class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        od=[0]*n
        
        d=defaultdict(list)
        q=[]
        
        for i in range(n):
            od[i]=len(graph[i])
            if not od[i]:
                q.append(i)
            for j in graph[i]:
                d[j].append(i)
        
        for terminal in q:
            for i in d[terminal]:
                
                od[i]-=1
                if not od[i]:
                    q.append(i)
                    
        return sorted(q)