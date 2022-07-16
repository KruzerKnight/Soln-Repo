class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]]!=t[i]:
                    return False
            elif t[i] in d.values():
                #print(1)
                return False
            else:
                d[s[i]]=t[i]
            #print(s[i],t[i],d,d.keys())
        return True