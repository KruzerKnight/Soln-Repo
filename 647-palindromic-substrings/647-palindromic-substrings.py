class Solution:
    def countSubstrings(self, s: str) -> int:
        def kruz(i,j):
            c=0
            l=len(s)
            while i>=0 and j<l and s[i]==s[j]:
                i-=1
                j+=1
                c+=1
            return c
        return sum(kruz(i,i)+kruz(i,i+1) for i in range(len(s)))