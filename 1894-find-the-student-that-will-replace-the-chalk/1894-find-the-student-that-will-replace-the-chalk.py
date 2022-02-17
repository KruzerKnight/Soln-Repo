class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s=sum(chalk)
        r=k%s
        rs=0
        for i in range(len(chalk)):
            if rs>r:
                return i-1
            rs+=chalk[i]
        return i