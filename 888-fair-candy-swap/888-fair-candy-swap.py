class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        s1,s2=sum(aliceSizes),sum(bobSizes)
        s=(s1-s2)//2
        A = set(aliceSizes)
        for b in set(bobSizes):
            if s + b in A:
                return [s + b, b]