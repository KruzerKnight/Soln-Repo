class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        e,o=0,len(nums)-1
        while e<o:
            if nums[e]%2!=0:
                nums[e],nums[o]=nums[o],nums[e]
                e-=1
                o-=1
            e+=1  
        return nums