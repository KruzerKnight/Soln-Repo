
# own solution
class Solution:
    def maxPower(self, s: str) -> int:
        power=1
        for i in range(1,len(s)):
            j=1
            while i<len(s) and s[i]==s[i-1]:
                j+=1
                i+=1
            power=max(power,j)
        return power

#faster solution
# class Solution:
#     def maxPower(self, s: str) -> int:
#         char = s[0]
#         max_len = 1
#         tmp_len = 1
#         for i in range(1,len(s)):
#             if s[i] == char:
#                 tmp_len +=1
#                 max_len = max(max_len, tmp_len)
#             else:
#                 char = s[i]
#                 tmp_len = 1


#         return max_len
