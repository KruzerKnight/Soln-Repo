class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d1=defaultdict(int)
        d2=defaultdict(int)
        for i in s:
            d1[i]+=1
        for i in t:
            d2[i]+=1
        #print(d1,d2)
        for i in d2:
            if i not in d1:
                return i
            if d1[i]!=d2[i]:
                return i