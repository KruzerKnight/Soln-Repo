class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        j=0
        n=len(name)
        m=len(typed)
        for i in range(m):
            if j<n and name[j]==typed[i]:
                j+=1
            elif i==0 or typed[i]!=typed[i-1]:
                return False
        return j==n
            