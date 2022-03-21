class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0)==0:
            pro=1
            for i in nums:
                pro*=i
            l=[]
            for j in nums:
                l.append(pro//j)
            return l
        elif nums.count(0)==1:
            pro=1
            l=[]
            for i in range(len(nums)):
                if nums[i]!=0:
                    pro*=nums[i]
                    
                else:
                    c=i
                l.append(0)
            l[c]=pro
            return l
        else:
            return [0]*len(nums)