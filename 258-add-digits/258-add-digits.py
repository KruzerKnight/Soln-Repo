class Solution(object):
    def addDigits(self, n):
        """
        :type num: int
        :rtype: int
        """
        while(n>=10):
            c=0
            s=str(n)
            for i in s:
                c+=int(i)
            n=c
        return n