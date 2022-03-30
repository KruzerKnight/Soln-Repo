class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        #my solution
        # for i in range(len(arr)-1):
        #     arr[i]=max(arr[i+1:])
        # arr[-1]=-1
        # return arr
        maxi=-1
        for i in range(len(arr)-1,-1,-1):
            arr[i],maxi=maxi,max(maxi,arr[i])
        
        return arr
        
        #here we go from backwards since each element checks for max and the maximum is substituted in a single traversal it is O(n)