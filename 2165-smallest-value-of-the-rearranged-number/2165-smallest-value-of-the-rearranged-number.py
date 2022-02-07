class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        if(num<0):
            s=list(str(num))
            s2=s[1::]
            s2.sort()
            s[1::]=s2[::-1]
            return int(''.join(s))
        s=list(str(num))
        if(len(s)==1):
            return int(s[0])
        z=s.count('0')
        s.sort()
        r=str(int(s[z])*(10**z))+''.join(s[z+1::])
        return int(r)