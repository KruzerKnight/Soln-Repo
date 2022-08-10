class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        d=defaultdict(list)
        count=0
        for i in range(len(nums)):
            v=d[nums[i]]
            #print(d,v)
            for j in v:
                #print(j*i%k,j,i,k,count)
                if j*i%k==0:
                    count+=1
            d[nums[i]].append(i)
        #print(d)
        return count