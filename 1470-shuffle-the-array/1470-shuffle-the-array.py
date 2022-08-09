class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l1=nums[:n]
        l2=nums[n:]
        nums=[0]*n*2
        #print(nums,l1,l2)
        nums[::2]=l1
        nums[1::2]=l2
        return nums