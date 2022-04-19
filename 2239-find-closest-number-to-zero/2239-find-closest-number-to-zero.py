class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        small=float(-inf)
        for i in nums:
            if abs(i)<=abs(small):
                if abs(i)==abs(small) and i<small:
                    continue
                small=i
        return small