class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1],nums[-3]*nums[-2]*nums[-1])
        
        
        # Test Cases are damn iriitating
        # note for negative number [-10,-9,-1,-2,-8] [-3,-100,-5,1]