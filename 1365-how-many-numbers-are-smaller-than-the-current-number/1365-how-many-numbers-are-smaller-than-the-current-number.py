class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        d=defaultdict(int)        
        for i in nums:
            d[i]+=1
        
        r=defaultdict(int)
        for i in d:
            for j in d:
                if i!=j and j<i:
                    r[i]+=d[j]
        
        res=[]
        for i in nums:
            res.append(r[i])
            
        return res