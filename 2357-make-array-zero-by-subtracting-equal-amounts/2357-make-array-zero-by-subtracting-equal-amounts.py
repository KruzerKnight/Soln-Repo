class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def removezero():
            while 0 in nums:
                nums.remove(0)
        m=max(nums)
        removezero()
        count=0
        while m>0:
            count+=1
            mini=min(nums)
            for i in range(len(nums)):
                nums[i]-=mini
            m=max(nums)
            removezero()
        return count