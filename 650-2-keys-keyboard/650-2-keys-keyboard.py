class Solution:
    def minSteps(self, n: int) -> int:
        def f(n):
            i=2
            while i*i<=n:
                while n%i==0:
                    n=n//i
                    yield i
                i+=1
            if n>1:
                yield n
        return sum(f(n))
    
    
#     def minSteps(self, n):
#     def factors(n):
#         d = 2
#         while d * d <= n:
#             while n % d == 0:
#                 n /= d
#                 yield d
#             d += 1
#         if n > 1:
#             yield n

#     return sum(factors(n))