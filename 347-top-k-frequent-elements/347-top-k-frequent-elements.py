class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=[]
        for i in d:
            l.append([i,d[i]])
        l.sort()
        l.sort(key=lambda x:x[1])
        res=[]
        for i in range(len(l)-1,len(l)-1-k,-1):
            res.append(l[i][0])
        return res
    
    # faster solution
# from collections import Counter
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]: 
#         # O(1) time 
#         if k == len(nums):
#             return nums
        
#         # 1. build hash map : character and how often it appears
#         # O(N) time
#         count = Counter(nums)   

#         # O(N) time
#         return [x[0] for x in count.most_common(k)]
