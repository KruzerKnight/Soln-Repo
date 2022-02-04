class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={0:-1}                        #dict is initialized with -1 cause then only the values from start is also considered like [0,1] and [1,0]
        count=0
        maxi=0
        for i,n in enumerate(nums,0):   #enumerate here iterates through nums (list) and iterates i (its index)
            if(n==1):
                count+=1
            else:
                count-=1
            if count in d:
                maxi=max(maxi,i-d[count])
            else:
                d[count]=i
        return maxi
   # To find the maximum length, we need a dict to store the value of count (as the key) and its associated index (as the value). We only need to save a count value and its index at the first time, when the same count values appear again, we use the new index subtracting the old index to calculate the length of a subarray. A variable maxi is used to to keep track of the current maximum length.
