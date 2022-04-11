class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd,even=[],[]
        for i in nums:
            if i%2==0:
                even.append(i)
            else:
                odd.append(i)
        nums[::2]=even
        nums[1::2]=odd
        return nums