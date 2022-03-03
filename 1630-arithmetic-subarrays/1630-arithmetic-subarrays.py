class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ll=[]
        for i in range(len(l)):
            if r[i]-l[i]>=1:
                s=nums[l[i]:r[i]+1]
                s.sort()
                d=s[1]-s[0]
                n=len(s)
                nn=0
                for j in range(1,n-1):
                    if s[j+1]-s[j]==d:
                        nn+=1
                    else:
                        print('1')
                        ll.append(False)
                        break
                if nn==n-2:
                    ll.append(True)
            else:
                ll.append(False)
        return ll