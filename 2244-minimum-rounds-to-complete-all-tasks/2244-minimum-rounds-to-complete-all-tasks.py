class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d=defaultdict(int)
        
        for i in tasks:
            d[i]+=1
        res=0
        #print(d)
        for i in d:
            if d[i]==1:
                return -1
            else:
                res+=(d[i]+2)//3
            
        return res