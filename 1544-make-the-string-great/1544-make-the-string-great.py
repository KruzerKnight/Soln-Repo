def cakeGood(s: str) -> str:
    for i in range(len(s)-1):
        if s[i].lower()==s[i+1].lower():
            if (s[i].islower() and s[i+1].islower()) or (s[i].isupper() and s[i+1].isupper()):
                continue
            return cakeGood(s[:i]+s[i+2:])
    return s
class Solution:
    
    def makeGood(self, s: str) -> str:
        return cakeGood(s)
    
#     fastest solution
#     class Solution:
#     def makeGood(self, s: str) -> str:
#         stack = []
#         for char in s:
#             if stack and stack[-1].lower() == char.lower() and stack[-1].isupper() != char.isupper():
#                 stack.pop()
#             else:
#                 stack.append(char)
#         return "".join(stack)
