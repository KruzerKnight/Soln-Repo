#naive diagonal accessing

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n=len(mat)
        sums=0
        for i in range(n):
            for j in range(n):
                if(i==j):
                    sums+=mat[i][j]
                elif(i+j==n-1 and i!=j):
                    sums+=mat[i][j]
        return sums
