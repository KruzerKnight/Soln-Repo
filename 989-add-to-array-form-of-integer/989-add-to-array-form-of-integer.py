class Solution:
    def addToArrayForm(self, digits: List[int], k: int) -> List[int]:
        n=len(digits)
        for i in range(n):
            digits[i]=str(digits[i])
        num=int(''.join(digits))+k
        return list(str(num))