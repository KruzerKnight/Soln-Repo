class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if(len(prices)<2):
            return 0
        maxi=-inf
        b=prices[0]
        s=prices[1]
        pro=s-b
        for j in range(len(prices)):
            b=min(b,prices[j])
            pro=prices[j]-b
            maxi=max(pro,maxi)
        return maxi