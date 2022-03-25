class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        s=sum(nums)
        ss=0
        l=[]
        for i in sorted(nums,reverse=True):
            #print(i,ss,s-ss)
            ss+=i
            l.append(i)
            if ss>s-ss:
                return sorted(l,reverse=True)