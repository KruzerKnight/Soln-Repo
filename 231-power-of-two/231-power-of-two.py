# a number which is a multiple of 2, in its binary form has only one 1 in it 

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        s=str(bin(n)[2:])
        if s.count('1')==1 and n>0:
            return True