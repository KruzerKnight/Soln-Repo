class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        if target not in nums:
            return []
        l=[]
        for j in range(nums.index(target),len(nums)):
            if nums[j]==target:
                l.append(j)
            else:
                break
        return l