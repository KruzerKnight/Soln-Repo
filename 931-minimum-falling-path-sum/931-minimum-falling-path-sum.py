import math
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for row in range(1, len(matrix)):
            for col in range(len(matrix)):
				# Update current element with the min of its upper 3 elements. 
				# If any of those do not exist then just use math.inf as placeholder
                matrix[row][col] = matrix[row][col] + \
				min(matrix[row-1][col], 
				matrix[row-1][col-1] if col - 1 >= 0 else math.inf, 
				matrix[row-1][col+1] if col + 1 < len(matrix) else math.inf)
		# The minimum item on the last row is the result because it is the "smallest path sum"
        return min(matrix[-1])