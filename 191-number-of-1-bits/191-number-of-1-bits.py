class Solution:
    def hammingWeight(self, n: int) -> int:
        n=str(bin(n)[2:])
        return n.count('1')

#Think of a number in binary n = XXXXXX1000, n - 1 is XXXXXX0111. n & (n - 1) will be XXXXXX0000 which is just remove the last significant 1    
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         count = 0
#         while(n>0):
#             n = n & (n-1)
#             count += 1
#         return count

#   another faster solution is
# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         s = bin(n)
#         c = 0
#         for i in range(2,len(s)):
#             if s[i] == "1":
#                 c += 1 
#         return c
