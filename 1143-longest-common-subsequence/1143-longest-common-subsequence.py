class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1=len(text1)
        l2=len(text2)
        c=[[-1 for i in range(l2+1)] for i in range(l1+1)]
        for j in range(l2+1):
            c[0][j] = 0
            
        for i in range(l1+1):
            c[i][0] = 0 
        
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if text1[i-1]==text2[j-1]:
                    c[i][j]=1+c[i-1][j-1]
                else:
                    c[i][j]=max(c[i-1][j],c[i][j-1])
        return c[l1][l2]