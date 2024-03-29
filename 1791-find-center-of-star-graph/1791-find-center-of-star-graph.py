class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d=defaultdict(int)
        for i in edges:
            d[i[0]]+=1
            d[i[1]]+=1
        return max(zip(d.values(),d.keys()))[1]
    
#faster solution:

#         [a] = set(edges[0]) & set(edges[1])
#         return a