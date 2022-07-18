class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        answer=[0,0]
        for i in d:
            if d[i]%2!=0:
                answer[1]+=1
            answer[0]+=d[i]//2
        return answer