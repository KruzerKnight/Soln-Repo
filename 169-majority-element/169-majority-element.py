class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        ele=0
        for i in nums:
            if c==0:
                ele=i
            if i==ele:
                c+=1
            else:
                c-=1
        return ele
     
        
        #my first submission, other one is from placement class moore's algorithm
        # d={}
        # for i in nums:
        #     if i in d:
        #         d[i]+=1
        #     else:
        #         d[i]=1
        # return max(zip(d.values(),d.keys()))[1]