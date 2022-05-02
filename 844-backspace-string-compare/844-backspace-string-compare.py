class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i=len(s)-1
        j=len(t)-1
        
        shc=0 #s hash count
        thc=0
        
        while i>=0 or j>=0:
            while i>=0: #finds a valid character
                #print('loop1',s[i])
                if s[i] == '#':
                    shc+=1
                    i-=1
                elif shc>0:
                    shc-=1
                    i-=1
                else:
                    break
            while j>=0:
                #print('loop2',t[j])
                if t[j] == '#':
                    thc+=1
                    j-=1
                elif thc>0:
                    thc-=1
                    j-=1
                else:
                    break
            if i>=0 and j>=0 and s[i]!=t[j]: #checks whether they are 
                return False
            if (i>=0)!=(j>=0):
                return False
            i-=1
            j-=1
        return True
        
        # O(n) space
        # s1=[]
        # for i in s:
        #     if i!='#':
        #         s1.append(i)
        #     elif s1:
        #         s1.pop()
        # s=''.join(s1)
        # s1=[]
        # for i in t:
        #     if i!='#':
        #         s1.append(i)
        #     elif s1:
        #         s1.pop()
        # t=''.join(s1)
        # return s==t