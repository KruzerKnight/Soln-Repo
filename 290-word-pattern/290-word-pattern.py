class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l=list(s.split(" "))
        #print(l)
        d={}
        if len(l)!=len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]]!=l[i]:
                    #print(d,i,pattern[i],d[pattern[i]],l[i])
                    return False
            elif l[i] in d.values():
                return False
            else:
                d[pattern[i]]=l[i]
        return True