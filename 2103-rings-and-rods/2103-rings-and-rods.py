class Solution:
    def countPoints(self, rings: str) -> int:
        count=0
        for i in range(10):
            
            r=0
            g=0
            b=0
            for j in range(0,len(rings),2):
                if rings[j]=='R' and r!=1:
                    if rings[j+1]==str(i):
                        r=1
                if rings[j]=='B' and b!=1:
                    if rings[j+1]==str(i):
                        b=1
                if rings[j]=='G' and g!=1:
                    if rings[j+1]==str(i):
                        g=1
                if r==1 and g==1 and b==1:
                    count+=1
                    break
        return count
    
    
# from collections import defaultdict
# class Solution:
#     def countPoints(self, rings: str) -> int:
#         d = defaultdict(set)
#         i = 0
#         while i < len(rings)-1:
#             d[rings[i+1]].add(rings[i])
#             i += 2
#         res = 0
#         for key in d:
#             if len(d[key]) == 3: res += 1
#         return res


# h = defaultdict(set)
# for i in range(0, len(rings) - 1, 2):
# 	h[rings[i + 1]].add(rings[i])
# return sum(len(v) == 3 for v in h.values())
