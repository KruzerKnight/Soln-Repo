class Solution:
    def countDigits(self, num: int) -> bool:
        count=0
        i=0
        x=num
        while(x>0):
            i+=1
            d=x%10
            x=x//10
            if d and num%d==0:
                count+=1
        return count==i
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        r=[]
        for i in range(left,right+1):
            if self.countDigits(i):
                r.append(i)
        return r