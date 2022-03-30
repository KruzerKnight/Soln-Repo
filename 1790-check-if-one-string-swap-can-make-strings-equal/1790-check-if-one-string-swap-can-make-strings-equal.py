class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff=0
        d1=defaultdict(lambda:0)
        d2=defaultdict(lambda:0)
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                diff+=1
            d1[s1[i]]+=1
            d2[s2[i]]+=1
        
        for i in d1:
            if d1[i]!=d2[i]:
                return False
        
        if diff<=2:
            return True
        return False
    