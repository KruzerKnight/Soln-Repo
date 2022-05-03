class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l=sorted(nums)
        count=0
        mini,maxi=len(nums),0
        for i in range(len(nums)):
            if l[i]!=nums[i]:
                count+=1
                mini=min(mini,i)
                maxi=max(maxi,i)
        if count:
            return(maxi-mini+1)
        else:
            return 0