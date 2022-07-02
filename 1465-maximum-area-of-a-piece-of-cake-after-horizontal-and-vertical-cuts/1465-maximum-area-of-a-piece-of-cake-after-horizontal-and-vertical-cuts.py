class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        hc.sort()
        vc.sort()
        dif0=[hc[0]]+[hc[i]-hc[i-1] for  i in range(1,len(hc))]+[h-hc[-1]]
        dif1=[vc[0]]+[vc[i]-vc[i-1] for  i in range(1,len(vc))]+[w-vc[-1]]
        
        mod=1000000007
        maxi=0
        maxi=max(dif0)*max(dif1)
        #print(dif0,dif1)
        return maxi%mod