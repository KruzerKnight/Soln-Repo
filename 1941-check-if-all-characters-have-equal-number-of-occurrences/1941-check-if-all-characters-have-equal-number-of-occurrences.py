class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        if len(set(d.values()))==1:
            return True
        return False
    
# alternative methods    
# class Solution:
# def areOccurrencesEqual(self, s: str) -> bool:
#     f = s.count(s[0])
#     for i in set(list(s)):
#         if s.count(i) != f:
#             return False
#     return True


# class Solution:
#     def areOccurrencesEqual(self, s: str) -> bool:
#         return len(set(Counter(s).values())) == 1
