class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*n
        r=0
        for i in range(2,n):
            if nums[i-1]-nums[i-2]==nums[i]-nums[i-1]:
                dp[i]=dp[i-1]+1
            r+=dp[i]
        return r