class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        d=defaultdict(int)
        for i in range(0,len(nums)-1):
            if nums[i]==key:
                d[nums[i+1]]+=1
        sd = {key: value for (key, value) in sorted(d.items(), key=lambda x: x[1], reverse=True)}
        #print(d,sd)
        return list(sd)[0]