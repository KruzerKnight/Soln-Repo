class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s=sum(nums)
        s1=0
        for i in range(len(nums)):
            if s1==s-nums[i]:
                return i
            s1+=nums[i]
            s-=nums[i]
        return -1