class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res=0
        if len(timeSeries)==0:
            return res
        for i in range(1,len(timeSeries)):
            res+=min(timeSeries[i]-timeSeries[i-1],duration)
        return res+duration