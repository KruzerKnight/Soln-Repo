class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        i=0
        st=1
        while(st<=n):
            st=3**i
            if(st==n):
                return True
            i+=1
# faster approach same logic
# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         a=1
#         if a==n:
#             return True
#         if n%3!=0:
#             return False
#         while a<=n:
#             if n==a:
#                 return True
#             a*=3
#         return False


# faster approach diff logic
# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         if(n<1):
#             return False
#         while(n%3==0):
#             n = n/3
#         return n==1
# fastest approach


# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         return True if n > 0 and (3**19) % n == 0 else False
