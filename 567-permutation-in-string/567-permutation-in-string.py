class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        d={}
        n=len(s1)
        for i in s1:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        sort=sorted(s1)
        for i in range(len(s2)-len(s1)+1):
            s=s2[i:i+n]
            if(sorted(s)==sort):
                return True
        return False