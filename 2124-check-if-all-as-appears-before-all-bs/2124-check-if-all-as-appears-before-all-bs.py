class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.rfind('a')>s.find('b') and s.count('a') and s.count('b'):
            return False
        return True