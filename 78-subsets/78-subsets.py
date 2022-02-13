class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l=[[]]
        x=[]
        temp=[]
        n=len(nums)
        for i in range(1,2**n):
            x.append(bin(i)[2:])
        for i in x:
            temp=[]
            y=i[::-1]
            for j in range(len(i)):
                if int(y[j]):
                    temp.append(nums[j])
            l.append(temp)
        return l