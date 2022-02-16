class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        s=str(bin(n)[2:])
        if(s.count('1'))==1 and n>0:
            if(len(s)%2!=0):
                return True
# faster solution
# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         if n == 1:
#             return True
#         if n < 1:
#             return False
#         return self.isPowerOfFour(n / 4)

# another faster solution
# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
        
#         if n <= 0:
#             return False
        
#         power = ceil(math.log(n, 4))
        
#         return math.pow(4, power) == n
