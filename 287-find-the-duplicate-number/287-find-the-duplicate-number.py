class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            nums[nums[i]%n]+=n
        #print(nums)
        for i in range(n):
            if nums[i]//n>1:
                return i
        
        # nums[i]%n provides a index lesser than n, so we add n to it
        # and we do it for all elements thus when a element is repeated, it would have been 
        # added by multiple n's, thus nums[i]//n will be greater than 1 for duplicate value