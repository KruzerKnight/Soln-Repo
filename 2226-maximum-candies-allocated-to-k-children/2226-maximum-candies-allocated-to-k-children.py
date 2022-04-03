class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies)<k:
            return 0
        elif sum(candies)==k:
            return 1
        left,right=0,sum(candies)//k
        while left<right:
            mid=(left+right+1)//2
            if k>sum(a//mid for a in candies):
                right=mid-1
            else:
                left=mid
        return left