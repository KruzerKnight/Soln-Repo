class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d={}
        for i in sorted(arr):
            d.setdefault(i,len(d)+1)
        return map(d.get,arr)