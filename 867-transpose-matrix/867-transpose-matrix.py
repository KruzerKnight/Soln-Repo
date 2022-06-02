class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        x=len(matrix)
        y=len(matrix[0])
        l=[]
        for i in range(y):
            r=[]
            for j in range(x):
                r.append(matrix[j][i])
            l.append(r)
        return l
                