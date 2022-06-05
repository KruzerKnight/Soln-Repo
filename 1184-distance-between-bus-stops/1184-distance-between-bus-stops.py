class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        s1=sum(distance)
        s=min(start,destination)
        d=max(start,destination)
        s2=sum(distance[s:d])
       # print(s,s2,s1-s2)
        return min(abs(s1-s2),s2)