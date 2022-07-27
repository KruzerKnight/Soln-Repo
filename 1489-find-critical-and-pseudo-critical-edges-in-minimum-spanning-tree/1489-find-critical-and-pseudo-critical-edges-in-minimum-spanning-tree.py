class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False
        if self.rank[pu] < self.rank[pv]:
            self.parent[pu] = self.parent[pv]
        elif self.rank[pu] > self.rank[pv]:
            self.parent[pv] = self.parent[pu]
        else:
            self.rank[pu] += 1
            self.parent[pv] = pu
        return True
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        edges=[[a,b,c,i] for i, [a,b,c] in enumerate(edges)]
        edges.sort(key=lambda x:x[2])
        
        def krus(n,edges,ban,inc):
            uf=UnionFind(n)
            w=0
            if inc!=-1:
                n-=1
                a,b,c,_=edges[inc]
                uf.union(a,b)
                w+=c
            for i,(a,b,c,_) in enumerate(edges):
                if i==ban:
                    continue
                if uf.union(a,b):
                    w+=c
                    n-=1
                if n==1:
                    break
            return float('inf') if n>1 else w
        
        ce=[] #criticalEdges
        mst=krus(n,edges,-1,-1)
        for i in range(len(edges)):
            twt=krus(n,edges,i,-1)
            if twt>mst:
                ce.append(edges[i][3])
        pe=[] #psuedoEdges
        for i in range(len(edges)):
            if edges[i][3] in ce:
                continue
            twt=krus(n,edges,-1,i)
            if twt==mst:
                pe.append(edges[i][3])
        
        return(ce,pe)