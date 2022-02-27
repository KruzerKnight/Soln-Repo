class Solution:
    
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        lo, hi = 1, totalTrips * min(time)

        def f(x):
            return sum(x // t for t in time) >= totalTrips

        while lo < hi:
            mid = (lo + hi) // 2
            if not f(mid): lo = mid + 1
            else: hi = mid
        return lo
    
#     For any time x, we can have total trips = Σ(x / time[i]) where i in [0, time.size())
# We need to minimize the above mentioned function total trips such that it is greater than or equal to the given variable totalTrips.
# We can use binary search.
# During the contest I got away with keeping lo = 1 and hi = 10 ^ 15
# On further inspection of the problem we can deduce that max value of x can be min(times) * totalTrips . So that can be used as hi