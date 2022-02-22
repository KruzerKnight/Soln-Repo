class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        for i in range(n):
            digits[i]=str(digits[i])
        num=int(''.join(digits))+1
        return list(str(num))