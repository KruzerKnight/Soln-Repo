class Solution:
    def reverseBits(self, n: int) -> int:
        n=str(bin(n)[2:])
        n=n[::-1]
        if(len(n)<32):
            n=list(n)
            n=n+['0']*(32-len(n))
            n=''.join(n)
        return int(n,2)
# another method
# class Solution:
#     def reverseBits(self, n: int) -> int:
#         ret, power = 0, 31
#         while n:
#             ret += (n & 1) << power
#             n = n >> 1
#             power -= 1
            
#         return ret
