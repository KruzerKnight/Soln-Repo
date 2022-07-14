class Solution:
    def fillCups(self, amount: List[int]) -> int:
        r=0
        amount.sort()
        while amount[2]!=0:
            r+=1
            if amount[1]!=0:
                amount[1]-=1
            amount[2]-=1
            amount.sort()
        return r

# we have to check the highest no of unfilled cups and want to make the process as parallel as possible, that is filling 2 cups as maximum as possible. 5 4 4 in that we fill 3 cups of first four then 2 cups of second four, so the 1 and 2 of 4(b and c) cups can be filled as 2 steps