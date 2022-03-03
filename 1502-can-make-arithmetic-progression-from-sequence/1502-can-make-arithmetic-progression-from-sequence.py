class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n=len(arr)
        nn=0
        d=(max(arr)-min(arr))//(n-1)
        j=min(arr)
        for i in range(len(arr)):
            if j in arr:
                nn+=1
                j+=d
            else:
                return False
        if n==nn:
            return True
# If its an arithmetic Sequence then the difference will be equal to
# the difference between the last and first element divided by no of elements -1
# i.e
# d=a[0]-a[n]//n-1
# so instrad of sorting we take min and max element find the differene adding it to the minimum element for n times should represent every element in the given
#array otherwise it is not an AP