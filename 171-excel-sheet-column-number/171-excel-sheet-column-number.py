class Solution:
    def titleToNumber(self, s: str) -> int:
        n=len(s)
        return sum((ord(s[i])-64)*(26**(n-i-1)) for i in range(n))
    
    
# return sum((ord(ch)-64)*26**i for i,ch in enumerate(reversed(columnTitle)))


# def titleToNumber(self, s: str) -> int:
#     result = 0
#     for char, i in zip(s, range(len(s), 0, -1)):
#         result += 26 ** (i-1) * (ord(char) - 64)
#     return result