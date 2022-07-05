 # key points : m = number of rows, n = number of colms
 # rotate 90 deg once ->   i, j <--> j,  n - i - 1
 # rotate 90 deg twice ->  i, j <--> m - i - 1, n - j - 1 
 # rotate 90 deg thrice -> i, j <--> n - j - 1, i
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        m=len(mat)
        n=len(mat[0])
        one,two,three,four=True,True,True,True
        for i in range(m):
            for j in range(n):
                if mat[i][j]!=target[j][n-i-1]:
                    #print('hi')
                    one=False
                if mat[i][j]!=target[m-i-1][n-j-1]:
                    #print('hi')
                    two=False
                if mat[i][j]!=target[n-j-1][i]:
                    #print('hi')
                    three=False
                if mat[i][j]!=target[i][j]:
                    #print('hi')
                    four=False
        #print(one or two or three or four,one,two,three,four)
        return one or two or three or four