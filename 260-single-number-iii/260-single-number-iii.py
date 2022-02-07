class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        r=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in nums:
            if d[i]==1:
                r.append(i)
        return r
    #faster method, adding it to a set, if it is repeated again removed from set, thus elements repeated twice are removed
#     s=set()
#     for n in nums:
#         if not n in s:
#             s.add(n)
#         elif n in s:
#             s.remove(n)
#     return list(s)
