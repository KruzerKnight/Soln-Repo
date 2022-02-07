#faster solution
#thrice the sum of the set values subracted by sum of set values gives the answer
#return (sum(set(nums)) * 3 - sum(nums)) // 2

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
