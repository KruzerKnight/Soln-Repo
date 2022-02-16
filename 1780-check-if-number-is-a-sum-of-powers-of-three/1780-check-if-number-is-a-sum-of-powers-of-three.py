# The question basically asks if n can be represented with base 3 (similar to binary representation which uses 2 as a base).
# Simplest method of converting a number to binary (that I know of):

# Divide n by 2, prefix the remainder to binary representation of n
# n = quotient
# Repeat step 1 and 2 until n < 2
# The ony difference here is that all the numbers can be represented in base 2 number system since the remainder is either 0 or 1, but is case of 3, the remainders can be 0,1 or 2. So if at all the remainder is 2, we cannot represent n as sum of power 3.


class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n>1:
            n,r=divmod(n,3)
            if r==2: return False
        return True
    
# same code but without divmod is faster
# class Solution:
#     def checkPowersOfThree(self, n: int) -> bool:
#         while n > 0:
#             while n %3 == 0:
#                 n = n //3
#             if n % 3 == 2:
#                 return False
#             n = n-1
#         return True
