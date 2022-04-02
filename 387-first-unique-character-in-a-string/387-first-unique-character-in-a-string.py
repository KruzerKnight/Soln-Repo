class Solution:
    def firstUniqChar(self, s: str) -> int:
        r=-1
        d=defaultdict(int)
        for i in s:
            d[i]+=1
        l=[]
        for i in d:
            if(d[i]==1):
                l.append(s.index(i))
        if(len(l)!=0):
            r=min(l)
        return r