class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=max(nums)
        sum1=sum(set(nums))
        sum2=sum(nums)
        exp_sum=n*(n+1)//2
        if(sum1==exp_sum):
            miss_num=n+1
            exp_sum=miss_num*(miss_num+1)//2
        else:
            miss_num=exp_sum-sum1
        rep_num=sum2-exp_sum+miss_num
        return [rep_num,miss_num]
        