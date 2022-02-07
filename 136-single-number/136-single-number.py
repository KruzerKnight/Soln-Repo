class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in nums:
            if d[i]==1:
                return i
        #count frequency, return the element with frequency 1
#faster approach, xor ing a number x with x return 0, thus result will only contain single element
        
# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         res = nums[0]
#         for i in range(1,len(nums)):
#             res ^= nums[i]
#         return res
