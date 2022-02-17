class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d={}
        for i in words:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=[]
        for i in d:
            l.append([i,d[i]])
        l.sort()
        l=sorted(l,reverse=True,key=lambda x:x[1])
        res=[]
        for i in range(k):
            res.append(l[i][0])
        return res
    

#faster solution

# def topKFrequent(self, words: List[str], k: int) -> List[str]:
#         dict = {}
#         for x in words:
#             if x in dict:
#                 dict[x] += 1
#             else:
#                 dict[x] = 1
#         res = sorted(dict, key=lambda x: (-dict[x], x))
#         return res[:k]
    
# '-dict[x]' is a sorting key which means sort dictionary based on it's value, here is the number of frequency (negative means ascending order, default is descending order), 'x' is back up sorting key which means if dictionary's value are same then sort it based on the dictionary's key, here is the word alphabetic order (negative means ascending order, default is descending order)