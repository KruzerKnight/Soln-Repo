**Union Find Code**
```
class UnionFind:
def __init__(self, n):
self.parent = [i for i in range(n)]
self.rank = [1] * n
​
def find(self, u):
if u != self.parent[u]:
self.parent[u] = self.find(self.parent[u])
return self.parent[u]
​
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
```