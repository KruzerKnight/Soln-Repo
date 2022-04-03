class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        if current==correct:
            return 0
        h=int(correct[:2])-int(current[:2])
        m=int(correct[3:])-int(current[3:])
        dit=h*60+m
        count=0
        if dit>=60:
            count+=dit//60
            dit=dit%60
        if dit>=15:
            count+=dit//15
            dit=dit%15   
        if dit>=5:
            count+=dit//5
            dit=dit%5    
        if dit>=1:
            count+=dit//1
            dit=dit%1    
        return count