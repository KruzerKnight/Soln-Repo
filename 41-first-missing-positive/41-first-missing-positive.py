class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        r=max(max(nums),0)
        n=len(nums)
        s=set(nums)
        for i in range(1,r+2):
            if i not in s:
                return i