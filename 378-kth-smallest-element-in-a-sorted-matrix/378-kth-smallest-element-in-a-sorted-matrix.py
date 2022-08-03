class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])  # For general, the matrix need not be a square
        minHeap = []  # val, r, c
        for r in range(min(k, m)):
            heappush(minHeap, (matrix[r][0], r, 0))

        ans = -1  # any dummy value
        for i in range(k):
            ans, r, c = heappop(minHeap)
            if c+1 < n: heappush(minHeap, (matrix[r][c + 1], r, c + 1))
        return ans