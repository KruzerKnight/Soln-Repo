class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s=0
        l=[0]*len(nums)
        for i in range(len(nums)):
            s+=nums[i]
            l[i]=s
        return l