class Solution:
    def maximumCandies(self, A: List[int], k: int) -> int:
        left, right = 0, sum(A) // k
        while left < right:
            mid = (left + right + 1) // 2
            if k > sum(a // mid for a in A):
                right = mid - 1
            else:
                left = mid
        return left