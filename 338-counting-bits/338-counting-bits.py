class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(n+1):
            s=str(bin(i)[2:])
            l.append(s.count('1'))
        return l
    
#learn this
# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         ans = [0] * (n + 1)
#         for i in range(1, n + 1):
#             ans[i] = ans[i & (i - 1)] + 1
#         return ans

# another soln
# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         ans = [0,1]
#         for j in range(n and int(log2(n))):
#             ans += [i+1 for i in ans] 
#         return ans[:n+1]
