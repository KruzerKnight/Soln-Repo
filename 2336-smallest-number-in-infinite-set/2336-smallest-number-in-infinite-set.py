class SmallestInfiniteSet:

    def __init__(self):
        self.l=[]
        
        #according to the constraint upto 1000 operations even if all are pop max would be 1000 so we take up to 1000
        for i in range(1,1001):
            self.l.append(i)

    def popSmallest(self) -> int:
        x=min(self.l)
        self.l.remove(x)
        return x

    def addBack(self, num: int) -> None:
        if num not in self.l:
            self.l.append(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)