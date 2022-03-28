# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res=0
        def kruz(th,s):
            if th==None:
                return
            s+=str(th.val)
            if th.left==None and th.right==None:
                self.res+=int(s)
            kruz(th.left,s)
            kruz(th.right,s)
        kruz(root,'')
        return self.res
            