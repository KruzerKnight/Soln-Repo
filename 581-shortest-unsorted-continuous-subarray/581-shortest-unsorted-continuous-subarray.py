class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l=sorted(nums)
        count=[]
        for i in range(len(nums)):
            if l[i]!=nums[i]:
                count.append(i)
        if count:
            return(max(count)-min(count)+1)
        else:
            return 0