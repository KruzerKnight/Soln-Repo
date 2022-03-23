class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        loopcount=0
        while(target>startValue):
            loopcount+=1
            if target%2==0:
                target=target//2
            else:
                target+=1
        return startValue-target+loopcount