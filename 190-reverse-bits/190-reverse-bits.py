class Solution:
    def reverseBits(self, n: int) -> int:
        n=str(bin(n)[2:])
        n=n[::-1]
        if(len(n)<32):
            n=list(n)
            n=n+['0']*(32-len(n))
            n=''.join(n)
        return int(n,2)