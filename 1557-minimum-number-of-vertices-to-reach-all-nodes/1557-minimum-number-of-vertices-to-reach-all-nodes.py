class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        d=defaultdict(list)
        for b,a in edges:
            d[a].append(b)
        res=[]
        for i in range(n):
            if i not in d:
                res.append(i)
        return res
    

    
# A node that does not have any incoming edge can only be reached by itself.
# Any other node with incoming edges can be reached from some other node.
# We only have to count the number of nodes with zero incoming edges.

#thus the nodes are seperated such that they contain their incoming nodes, so the nodes which are not present in the dictionary doesnt have any incoming edges