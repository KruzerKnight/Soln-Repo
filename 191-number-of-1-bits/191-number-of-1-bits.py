class Solution:
    def hammingWeight(self, n: int) -> int:
        n=str(bin(n)[2:])
        return n.count('1')