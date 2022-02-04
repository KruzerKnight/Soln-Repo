class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={0:-1}
        count=0
        maxi=0
        for i,n in enumerate(nums,0):
            if(n==1):
                count+=1
            else:
                count-=1
            if count in d:
                maxi=max(maxi,i-d[count])
            else:
                d[count]=i
        return maxi