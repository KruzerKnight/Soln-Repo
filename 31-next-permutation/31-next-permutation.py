class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        #https://leetcode.com/problems/next-permutation/discuss/13907/easy-python-solution-based-on-lexicographical-permutation-algorithm/14319
        """
        r=len(nums)-1
        while nums[r]<=nums[r-1] and r-1>=0:
            r-=1
        if r==0:
            self.reverse(nums,0,len(nums)-1)
            return
        piv=r-1
        s=0
        
        for i in range(len(nums)-1,piv,-1):
            if nums[i]>nums[piv]:
                s=i
                break
        
        nums[piv],nums[s] = nums[s],nums[piv]
        self.reverse(nums,piv+1,len(nums)-1)
        
    def reverse(self,nums,l,r):
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l += 1
            r -= 1