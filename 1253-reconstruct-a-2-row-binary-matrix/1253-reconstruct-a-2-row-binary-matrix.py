class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        
        if upper+lower!=sum(colsum):
            return []
        
        u=upper
        d=lower
        n=len(colsum)
        lu=[0]*n
        ld=[0]*n
        for i in range(n):
            
            if colsum[i]==2:
                lu[i]=1
                ld[i]=1
                upper-=1
                lower-=1
            elif colsum[i]==0:
                lu[i]=0
                ld[i]=0
        
        for i in range(n):
            if upper>0 and colsum[i]==1:
                upper-=1
                lu[i]=1
                ld[i]=0
                
            elif lower>0 and colsum[i]==1:
                lu[i]=0
                ld[i]=1
                lower-=1
        if sum(lu)!=u or sum(ld)!=d:
            return []
        return [lu,ld]