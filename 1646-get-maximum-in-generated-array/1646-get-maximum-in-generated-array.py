class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        dp=[0]*(n+2)
        dp[0]=0
        if n>0: dp[1]=1
        for i in range(1,n):
            if 2*i<n:
                dp[2*i]=dp[i]
            else:
                break
            if 2*i+1<n+1:
                dp[2*i+1]=dp[i]+dp[i+1]
            else:
                break
        #print(dp)
        return max(dp)