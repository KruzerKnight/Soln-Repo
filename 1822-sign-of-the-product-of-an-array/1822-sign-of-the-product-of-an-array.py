class Solution:
    def arraySign(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            if i==0:
                return 0
            elif i<0:
                c+=1
        if c%2==0:
            return 1
        return -1