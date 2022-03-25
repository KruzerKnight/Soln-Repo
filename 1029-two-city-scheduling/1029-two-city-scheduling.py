class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        s=0
        l=[]
        for i in costs:
            s+=i[0]
            l.append(i[1]-i[0])
        l.sort()
        s+=sum(l[0:len(l)//2])
        return s