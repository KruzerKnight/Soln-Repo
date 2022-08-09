class OrderedStream:

    def __init__(self, n: int):
        self.l=['']*n
        self.ptr=0

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey-=1
        self.l[idKey]=value
        if idKey>self.ptr:
            return []
        while self.ptr<len(self.l) and self.l[self.ptr]!='':
            self.ptr+=1
        return self.l[idKey:self.ptr]
        
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)