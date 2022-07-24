class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n=len(matrix)
        m=len(matrix[0])
        
        for i in matrix:
            if i[0]<=target<=i[-1]:
                #print(i)
                start,end=0,m-1
                
                while start<=end:
                    mid=(start+end)//2
                    if target==i[mid]:
                        return True
                    elif i[mid]<target:
                        start=mid+1
                    else:
                        end=mid-1
        return False