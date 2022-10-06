class TimeMap:

    def __init__(self):
        self.t=defaultdict(list)
        self.v=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.t[key].append(timestamp)
        self.v[key].append(value)
        

    def get(self, key: str, timestamp: int) -> str:
        i=bisect.bisect(self.t[key], timestamp)
        return self.v[key][i - 1] if i else ''
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)