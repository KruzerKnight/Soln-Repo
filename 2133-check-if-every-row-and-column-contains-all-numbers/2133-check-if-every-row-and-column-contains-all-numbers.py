# first wee are comparing the length of rows with n, cause set(row) will be equal to n, when no elements are repeated
# then we use enumerate to add index to the element and add all the elements in a list to comapre in columns
# we sort it w.r.to index and now check the columns

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n=len(matrix)
        for i in matrix:
            if(len(set(i)))!=n:
                return False
        l=[]
        for i in matrix:
            ad=[[x,i] for i,x in enumerate(i)]
            l+=ad
        l=sorted(l, key= lambda x:x[1])         #sorted w.r.to the column numbers
        for j in range(n):
            count=0
            s=set()
            for k in range(j*n,(j+1)*n):        #iterating through the values from 0->n, n->2n
                i=l[k]
                if i[1]==j:
                    s.add(i[0])
            if(len(s)!=n):
                return False
        return True
