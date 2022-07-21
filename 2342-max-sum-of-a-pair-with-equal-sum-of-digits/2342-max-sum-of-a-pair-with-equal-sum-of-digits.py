class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        d={}
        maxi=-1
        for i in nums:
            s=0
            j=i
            while i>0:
                s+=i%10
                i=i//10
            if s not in d:
                d[s]=j
            else:
                
                maxi=max(maxi,d[s]+j)
                d[s]=max(d[s],j)
        return maxi