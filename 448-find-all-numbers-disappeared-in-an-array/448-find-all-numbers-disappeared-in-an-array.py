class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            ind=abs(nums[i])-1
            nums[ind]=-abs(nums[ind])
            #print(ind,nums)
        l=[]
        #print(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                l.append(i+1)
        
        return l
    
    #this is an O(n) approach with no extra space