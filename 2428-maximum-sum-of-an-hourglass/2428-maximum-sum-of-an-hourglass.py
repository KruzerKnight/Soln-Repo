class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxi=0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if j+2<len(grid[0]) and i+2<len(grid):
                    sums=grid[i][j]+grid[i][j+1]+grid[i][j+2]+grid[i+1][j+1]+grid[i+2][j]+grid[i+2][j+1]+grid[i+2][j+2]
                    maxi=max(maxi,sums)
                    # print(grid[i][j],grid[i][j+1],grid[i][j+2],grid[i+1][j+1],grid[i+2][j],grid[i+2][j+1],grid[i+2][j+2])
        return maxi