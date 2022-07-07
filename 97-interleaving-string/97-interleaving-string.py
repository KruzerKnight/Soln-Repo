
#redo

class Solution:
    def isInterleave(self, s1, s2, s3):
        @lru_cache(None)
        def dp(i, j):
            if i == -1 and j == -1: return True
            return (j >= 0 and s2[j] == s3[i+j+1] and dp(i, j-1)) or (i >= 0 and s1[i] == s3[i+j+1] and dp(i-1,j))
        
        return len(s1) + len(s2) == len(s3) and dp(len(s1) - 1, len(s2) - 1)