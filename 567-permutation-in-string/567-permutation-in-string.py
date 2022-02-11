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
    #faster method
#     class Solution(object):
    
#     def checkInclusion(self, s1, s2):
#         if len(s1) > len(s2):
#             return False
        
#         s1mp = [0] * 26
#         mp = [0] * 26

        
#         for ch in s1:
#             s1mp[ord(ch) - ord('a')] += 1
            
#         for i in range(len(s1)):
#             mp[ord(s2[i]) - ord('a')] += 1
           
        
#         i = 0
#         j = len(s1)
        
#         if s1mp == mp:
#             return True
        
#         while j < len(s2):
#             mp[ord(s2[i]) - ord('a')] -= 1
#             i += 1
#             mp[ord(s2[j]) - ord('a')] += 1
#             j += 1
#             if mp == s1mp:
#                 return True
#         return False
