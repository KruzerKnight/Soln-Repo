class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        n=len(digits)
        for i in range(n):
            num+=digits[i]*10**(n-i-1)
        num+=1
        return list(str(num))
        