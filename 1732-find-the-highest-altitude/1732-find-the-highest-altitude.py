class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxi=0
        count=0
        for i in gain:
            count+=i
            maxi=max(maxi,count)
        return maxi