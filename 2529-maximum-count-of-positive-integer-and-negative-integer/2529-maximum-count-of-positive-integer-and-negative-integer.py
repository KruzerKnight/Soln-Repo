class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        cn=0
        cp=0
        for i in nums:
            if i<0:
                cn+=1
            if i>0:
                cp+=1
        return max(cn,cp)