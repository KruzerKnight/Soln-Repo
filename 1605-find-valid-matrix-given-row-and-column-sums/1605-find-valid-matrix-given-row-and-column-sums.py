class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n=len(rowSum)
        m=len(colSum)
        
        a=[[0]*m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                a[i][j]=min(rowSum[i],colSum[j])
                rowSum[i]-=a[i][j]
                colSum[j]-=a[i][j]
        return a