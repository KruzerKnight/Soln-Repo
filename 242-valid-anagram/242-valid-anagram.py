class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        r=False
        d1={}
        d2={}
        for i in s:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1
        for i in t:
            if i not in d2:
                d2[i]=1
            else:
                d2[i]+=1
        if(len(d1)>len(d2)):
            dc1=d2
            dc2=d1
        else:
            dc1=d1
            dc2=d2
        for i in dc2:
            if i not in dc1:
                return False
            elif(dc1[i]==dc2[i]):
                continue
            return False
        return True