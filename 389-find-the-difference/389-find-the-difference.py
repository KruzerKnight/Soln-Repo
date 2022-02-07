class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d1={}
        d2={}
        for i in s:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        for i in t:
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1
        for i in d2:
            if i in d1:
                if(d1[i]!=d2[i]):
                    return i
            else:
                return i
#create two dictionaries and count the letters in both strings
#if the second dict has a element more then that is the extra one
#if not check the count 