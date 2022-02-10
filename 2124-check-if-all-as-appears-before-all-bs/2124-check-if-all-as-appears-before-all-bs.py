class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=list(s)
        l=l[::-1]
        s1=''.join(l)
        if(len(set(l))==1):
            return True
        if(len(s1)-s1.find('a'))>s.find('b'):
            return False
        return True