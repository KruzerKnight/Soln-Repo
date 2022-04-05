# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum=0
        def kruz(th,flag):
            if not th:
                return
            if th.left==None and th.right==None:
                if flag==-1:
                    self.sum+=th.val
            kruz(th.left,-1)
            kruz(th.right,1)
            return
        kruz(root,0)
        return self.sum