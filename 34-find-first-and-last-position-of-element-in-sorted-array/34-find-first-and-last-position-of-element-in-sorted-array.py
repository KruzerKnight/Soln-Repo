class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        else:
            x,y=0,len(nums)-1
            for i in range(len(nums)):
                if nums[i]==target:
                    x=i
                    break
            for i in range(x+1,len(nums)):
                if nums[i]>target:
                    y=i-1
                    break
            return [x,y]