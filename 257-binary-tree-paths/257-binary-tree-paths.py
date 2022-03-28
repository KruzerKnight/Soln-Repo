# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        l=[]
        def kruz(th,r):
            if th==None:
                return
            r+=str(th.val)+'->'
            #print(r)
            if th.left==None and th.right==None:
                l.append(r[:-2])
            kruz(th.left,r)
            kruz(th.right,r)
        kruz(root,'')
        return l