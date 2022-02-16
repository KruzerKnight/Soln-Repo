class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        s=str(bin(n)[2:])
        if(s.count('1'))==1 and n>0:
            if(len(s)%2!=0):
                return True