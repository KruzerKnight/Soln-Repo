class Solution:
    def countDigits(self, num: int) -> int:
        count=0
        x=num
        while(x>0):
            d=x%10
            x=x//10
            if d and num%d==0:
                count+=1
        return count