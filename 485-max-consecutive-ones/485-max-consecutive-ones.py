class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i=0
        n=len(nums)
        maxi=0
        while(i<n):
            j=0
            while i<n and nums[i]:
                j+=1
                i+=1
            maxi=max(maxi,j)
            i+=1
        return maxi