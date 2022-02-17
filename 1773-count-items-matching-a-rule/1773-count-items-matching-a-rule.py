class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey=="type":
            r=0
        elif ruleKey=="color":
            r=1
        else:
            r=2
        count=0
        for i in items:
            if(i[r]==ruleValue):
                count+=1
        return count