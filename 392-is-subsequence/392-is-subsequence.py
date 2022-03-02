class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        for k in s:
            for a in range(j,len(t)):
                if k not in t[j:]:
                    return False
                if t[a]==k:
                    j=a+1
                    i+=1
                    break
        if i==len(s):
            return True
        return False
            