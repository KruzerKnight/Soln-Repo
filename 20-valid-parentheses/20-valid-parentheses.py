class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        dic={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        ol=['(','{','[']
        cl=[')','}',']']
        for i in s:
            if i in ol:
                l.append(i)
            elif i in cl:
                if(not l or dic[i]!=l.pop()):
                    return False
        if(not l):
            return True