# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        l=[]
        def kruz(th,s):
            if th==None:
                return
            s+=th.val
            #print(th.val,s)
            if th.left==None and th.right==None:
                if targetSum==s:
                    l.append(True)
            kruz(th.left,s)
            kruz(th.right,s)
        kruz(root,0)
        return any(l)