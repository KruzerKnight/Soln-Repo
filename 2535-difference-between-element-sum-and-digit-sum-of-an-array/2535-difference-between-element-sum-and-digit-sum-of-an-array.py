class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele_sum=sum(nums)
        dig_sum=0
        for i in nums:
            while i>0:
                dig_sum+=i%10
                i=i//10
        return abs(ele_sum-dig_sum)