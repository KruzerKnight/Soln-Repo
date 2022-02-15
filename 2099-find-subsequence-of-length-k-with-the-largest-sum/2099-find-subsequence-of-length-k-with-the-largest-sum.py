class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        l=[[x,i] for i,x in enumerate(nums)]
        l=sorted(l,key= lambda keey:keey[0],reverse=True)
        k=l[:k]
        k=sorted(k,key= lambda keey:keey[1])
        k=[i[0] for i in k]
        return k