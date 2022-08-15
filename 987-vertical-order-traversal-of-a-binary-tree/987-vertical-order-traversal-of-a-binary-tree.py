# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d=defaultdict(list)
        def kruz(root,hd,l):
            if root==None:
                return
            d[hd].append([l,root.val])
            kruz(root.left,hd-1,l+1)
            kruz(root.right,hd+1,l+1)
        kruz(root,0,0)
        k=sorted(d)

        #print(d)
        l=[]
        for i in k:
            #print(d[i])
            r=[]
            for j in sorted(d[i]):
            
                r.append(j[1])
            l.append(r)
        return l
