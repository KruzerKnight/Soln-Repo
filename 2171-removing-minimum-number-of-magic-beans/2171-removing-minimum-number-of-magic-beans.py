class Solution(object):
    def minimumRemoval(self, beans):
        """
        :type beans: List[int]
        :rtype: int
        """
        tot=sum(beans)
        beans.sort()
        tt=0
        l=[]
        n=len(beans)
        for i in range(n):
            nx=tot-(n-i)*beans[i]
            l.append(nx+tt)
            tt+=beans[i]
            tot-=beans[i]
        return min(l)
    # O(n) solution
    # Sort the function so it becomes 1 4 5 6
    # Then if you choose a number x, we want to make elements in left side as 0
    # and right side elements as the number x
    # so if x=4
    # sum of left elements is 1
    # and the sum after making the elements to x in right side = (5-4)+(6-2) =3
    # Therefore, 3+1=4
    # like that whole list is traversed and the minimum is returned
    # choose x
    # taking the total sum so we can subract no of times the element remain right side * 8
    # that is (len(nums)-i)*x
    # and the sum of left elements is in tt