class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        max1,max0=0,0
        count1,count0=0,0
        fl1,fl0=0,0
        for i in range(len(s)):
            if(s[i]=='1'):
                if not fl1:
                    fl0=0
                    fl1=1
                    max0=max(max0,count0)
                    count0=0
                    count1+=1
                else:
                    count1+=1
            else:
                if not fl0:
                    fl1=0
                    fl0=1
                    max1=max(max1,count1)
                    count1=0
                    count0+=1
                else:
                    count0+=1
        max0=max(max0,count0)
        max1=max(max1,count1)
        return max1>max0
# instead of calculating at a time:
# Calculate seperately
# class Solution:
#     def checkZeroOnes(self, s: str) -> bool:
#         one = 0
#         zero = 0
        
#         i = 0
#         while i < len(s):
#             cur = 0
#             while i < len(s) and s[i]=='1':
#                 cur += 1
#                 i += 1
#             one = max(one,cur)
#             i += 1
            
#         i = 0
#         while i < len(s):
#             cur = 0
#             while i < len(s) and s[i]=='0':
#                 cur += 1
#                 i += 1
#             zero = max(zero,cur)
#             i += 1


# Otherwise split it along with 0s and 1s
# class Solution:
#     def checkZeroOnes(self, s: str) -> bool:
#         s1 = s.split('0')
#         s0 = s.split('1')
#         r1 = max([len(i) for i in s1])
#         r0 = max([len(i) for i in s0])
#         return r1>r0
