#Fastrer solution
# class Solution(object):
#     def findPairs(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         two_diff = set()
#         res = set()
#         for num in nums:
#             if num+k in two_diff:
#                 res.add((num, num+k))
#             if num-k in two_diff:
#                 res.add((num-k, num))
#             two_diff.add(num)
            
       
#         return len(res)

#####################
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=list(set(nums))
        count=0
        if(k==0):
            d={}
            for i in nums:
                if i in d:
                    d[i]+=1
                else:
                    d[i]=1
            for i in d:
                if(d[i]>=2):
                    count+=1
            return count
        l.sort()  
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                if(abs(l[i]-l[j])==k):
                    count+=1
                if(abs(l[i]-l[j])>k):
                    break
        return count
