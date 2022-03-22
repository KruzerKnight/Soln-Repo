class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        s=['a']*n
        k=k-n
        j=n-1
        while(k):
            if k<26:
                s[j]=chr(ord(s[j])+k)
                j-=1
                return ''.join(s)
            else:
                s[j]='z'
                k-=25
                j-=1
        return ''.join(s)