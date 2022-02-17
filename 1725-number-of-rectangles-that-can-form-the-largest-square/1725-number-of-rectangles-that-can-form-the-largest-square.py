class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        l=[]
        for i in rectangles:
            l.append(min(i))
        return l.count(max(l))