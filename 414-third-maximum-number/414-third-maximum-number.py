class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        l=list(set(nums))
        l.sort()
        if(len(l)==1):
            return l[0]
        elif(len(l)==2):
            return l[1]
        return l[-3]