class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(n+1):
            s=str(bin(i)[2:])
            l.append(s.count('1'))
        return l