class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        if len(roads)==0:
            return 0
        elif len(roads)==1:
            return 1
        d=defaultdict(list)
        
        for a,b in roads:
            d[a].append(b)
            d[b].append(a)
            
        maxi=0
        
        for i in range(n):
            for j in range(i+1,n):
                rank=len(d[i])+len(d[j])
                
                if i in d[j]:
                    rank-=1
                maxi=max(maxi,rank)
        return maxi
        