class Solution:
    def sortSentence(self, s: str) -> str:
        l=['']*len(s.split())
        for i in s.split():
            n=int(i[-1])
            long=len(i)
            l[n-1]=i[:-1]
        return ' '.join(l)
            