# faster method
# class Solution:
#     def hammingDistance(self, x: int, y: int) -> int:
#         z = bin( x ^ y )
#         return z.count('1')

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a=max(x,y)
        b=min(x,y)
        a=str(bin(a)[2:])
        b=str(bin(b)[2:])
        b='0'*(len(a)-len(b))+b
        count=0
        for i in range(len(a)):
            if(a[i]!=b[i]):
                count+=1
        return count
    
