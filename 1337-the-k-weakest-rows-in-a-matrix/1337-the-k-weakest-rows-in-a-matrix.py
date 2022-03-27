class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        for i in range(len(mat)):
            mat[i]=[mat[i].count(1),i]
        mat.sort()
        res=[]
        for j in range(k):
            res.append(mat[j][1])
        return res