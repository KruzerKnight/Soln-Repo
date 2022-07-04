class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        count=0
        pos=None
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i] and pos!=True:
                count+=1
                pos=True
            elif nums[i-1]>nums[i] and pos!=False:
                count+=1
                pos=False
        return count+1