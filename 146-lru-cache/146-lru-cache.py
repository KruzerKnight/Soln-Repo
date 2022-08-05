class LRUCache:

    def __init__(self, capacity: int):
        self.d=OrderedDict()
        self.cap=capacity

    def get(self, key: int) -> int:
        if key in self.d:
            ret=self.d.pop(key)
            self.d[key]=ret
            return ret
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d.pop(key)
        elif self.cap>0:
            self.cap-=1
        else:
            self.d.popitem(last=False)
        self.d[key]=value
        
        #print(self.d)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)