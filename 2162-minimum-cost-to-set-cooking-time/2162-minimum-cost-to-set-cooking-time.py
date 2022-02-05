class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, t: int) -> int:
        maxmin=t//60                            # I changed the default input as t
        mini=inf
        def costfinder(mins,sec):               # Afunction to calculate cost
            m,p,st=moveCost,pushCost,startAt
            res=0
            s=str(mins*100+sec)
            for i in s:
                if(int(i)==st):        #if the current position is same as required only pushCost is enough
                    res+=p
                else:
                    res+=p+m
                    st=int(i)
            return res
        for mins in range(maxmin+1):   # to check every possibility till max minute
            sec=t-mins*60
            if(mins>99 or sec>99):      # since only till 99 we can do
                continue
            mini=min(mini,costfinder(mins,sec))
        return mini