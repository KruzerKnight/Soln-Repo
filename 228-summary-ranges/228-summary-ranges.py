class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return []
        if len(nums)==1:
            return [str(nums[0])]
        start=nums[0]
        l=[]
        for i in range(0,len(nums)-1):
            if nums[i]==nums[i+1]-1:
                print(nums[i],nums[i+1]-1)
                continue
            elif(start==nums[i]):
                print(start)
                l.append(str(start))
                start=nums[i+1]
            else:
                print(start,nums[i],'3')
                s=[str(start),'->',str(nums[i])]
                l.append(''.join(s))
                start=nums[i+1]
        if nums[-1]==nums[-2]+1:
            s=[str(start),'->',str(nums[-1])]
            l.append(''.join(s))
        else:
            l.append(str(nums[-1]))
        return l