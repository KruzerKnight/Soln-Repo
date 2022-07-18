class Solution:
    def frequencySort(self, s: str) -> str:
        d=defaultdict(int)
        for i in s:
            d[i]+=1
        d = {key: value for (key, value) in sorted(d.items(), key=lambda x: x[1], reverse=True)}
        r=''
        for i in d:
            r+=d[i]*i
        return r