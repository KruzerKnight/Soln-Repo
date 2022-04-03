class Solution:
    #https://www.geeksforgeeks.org/ugly-numbers/
    def isUgly(self, num: int) -> bool:
        if num == 0: return False
        while num % 5 == 0: num /= 5
        while num % 3 == 0: num /= 3
        while num % 2 == 0: num /= 2
        return num == 1
#         ug=[0]*n
        
#         ug[0]=1
        
#         n2=2
#         n3=3
#         n5=5
        
#         i2=i3=i5=0
        
#         for i in range(1,n):
#             ug[i]=min(n2,n3,n5)
            
#             if ug[i]==n2:
#                 n2*=2
#                 i2+=1
#             if ug[i]==n3:
#                 n3*=3
#                 i3+=1
#             if ug[i]==n5:
#                 n5*=5
#                 i5+=1
#         return ug[-1]