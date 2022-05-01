class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1=[]
        for i in s:
            if i!='#':
                s1.append(i)
            elif s1:
                s1.pop()
        s=''.join(s1)
        s1=[]
        for i in t:
            if i!='#':
                s1.append(i)
            elif s1:
                s1.pop()
        t=''.join(s1)
        return s==t