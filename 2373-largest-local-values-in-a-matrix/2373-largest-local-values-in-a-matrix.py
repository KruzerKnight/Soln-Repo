class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0]*(n-2) for _ in range(m-2)]
        for i in range(m-2): 
            for j in range(n-2): 
                ans[i][j] = max(grid[ii][jj] for ii in range(i, i+3) for jj in range(j, j+3))
        return ans 