class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        
        m=max(d.values())
        r=[]
        for i in d:
            if d[i]==m:
                r.append(i)
        mini=len(nums)+1
        for i in r:
            mini=min(mini,abs(nums.index(i)-(len(nums)-nums[::-1].index(i))))
        
        return mini