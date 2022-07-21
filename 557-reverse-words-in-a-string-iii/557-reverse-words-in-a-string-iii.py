class Solution:
    def reverseWords(self, s: str) -> str:
        l=list(s.split())
        r=[]
        print(l)
        for i in l:
            rev=i[::-1]
            r.append(rev)
        return ' '.join(r)