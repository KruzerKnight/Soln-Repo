# a number which is a power of 2, in its binary form has only one 1 in it 

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        s=str(bin(n)[2:])
        if s.count('1')==1 and n>0:
            return True
# a faster solution 
# if we do x&-x if its a power of 2 it returns x, else returns 1
# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         if n == 0:
#             return False
#         return n & (-n) == n
