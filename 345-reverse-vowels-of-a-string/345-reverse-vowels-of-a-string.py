class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        vow=['a','e','i','o','u','A','E','I','O','U']
        l=[]
        for i in range(len(s)):
            if s[i] in vow:
                l.append(s[i])
                s[i]=0
        l=l[::-1]
        i=0
        for j in range(len(s)):
            if s[j]==0:
                s[j]=l[i]
                i+=1
        return ''.join(s)
                