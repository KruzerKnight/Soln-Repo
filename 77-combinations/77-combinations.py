class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums=[i for i in range(1,n+1)]
        return list(set(combinations(nums,k)))