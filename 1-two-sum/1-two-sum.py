class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r=[]
        for i in range(len(nums)):
            if(target-nums[i] in nums[:i]):
                return[i,nums.index(target-nums[i],0,i)]
            elif(target-nums[i] in nums[i+1:]):
                #print(1)
                return[i,nums.index(target-nums[i],i+1,len(nums))]