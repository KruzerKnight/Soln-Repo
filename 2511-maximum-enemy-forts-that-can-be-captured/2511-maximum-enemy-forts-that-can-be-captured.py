class Solution:
    def captureForts(self, forts: List[int]) -> int:
        m=0
        v='z'
        count=0
        for i in range(len(forts)):
            if forts[i]==1:
                if v=='x' or v=='z':
                    count=0
                elif v=='y':
                    m=max(m,count)
                    count=0
                v='x'
            elif forts[i]==0:
                count+=1
            else:
                if v=='y' or v=='z':
                    count=0
                elif v=='x':
                    m=max(m,count)
                    count=0
                v='y'
            
            #print(i,v,count)
        return m