class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums=0
        maxi=-inf
        for i in nums:
            sums+=i
            if(sums>maxi):
                maxi=sums
            
            if(sums<0):
                sums=0
        return maxi