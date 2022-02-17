class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d={}
        for i in words:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=[]
        for i in d:
            l.append([i,d[i]])
        l.sort()
        l=sorted(l,reverse=True,key=lambda x:x[1])
        res=[]
        for i in range(k):
            res.append(l[i][0])
        return res