class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        d=defaultdict(int)
        
        for i in nums1:
            d[i]+=1
        
        for j in nums2:
            if j in nums1 and d[j]>0:
                l.append(j)
                d[j]-=1
        return l