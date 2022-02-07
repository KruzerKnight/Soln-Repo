class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        r=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in nums:
            if d[i]==1:
                r.append(i)
        return r