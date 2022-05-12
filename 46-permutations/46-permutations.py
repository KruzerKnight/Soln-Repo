class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(set(permutations(nums)))