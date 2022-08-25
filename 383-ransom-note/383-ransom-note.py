class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r=False
        d1=defaultdict(lambda:0)
        d2=defaultdict(lambda:0)
        for i in magazine:
            d1[i]+=1
        for i in ransomNote:
            d2[i]+=1
        for i in d2:
            if i not in d1:
                return False
            elif(d1[i]>=d2[i]):
                continue
            return False
        return True