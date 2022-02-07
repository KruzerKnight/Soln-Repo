
#faster method using N(N+1)/2 formula
 #return len(nums) * (len(nums)+1) / 2 - sum(nums)

#naive method
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=max(nums)
        mini=min(nums)
        for i in range(mini,maxi):
            if i not in nums:
                return i
        if(mini-1>=0):
            return mini-1
        return maxi+1
        
        #checkout for edge cases
        #[1]
        #[0,1]
