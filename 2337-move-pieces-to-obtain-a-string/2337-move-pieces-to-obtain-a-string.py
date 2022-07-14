class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n=len(target)
        i,j=0,0
        while i<=n and j<=n:
            while i<n and start[i]=='_':
                i+=1
            while j<n and target[j]=='_':
                j+=1
            if i==n or j==n:
                return i==n and j==n
            if start[i]!=target[j]:
                return False
            elif start[i]=='L':
                if i<j:
                    return False
            else:
                if i>j:
                    return False
                
            i+=1
            j+=1
        return True