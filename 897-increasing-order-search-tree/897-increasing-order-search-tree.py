# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def kruz(th1,th2):
            if not th1:
                return th2
            res=kruz(th1.left,th1)
            th1.left=None
            th1.right=kruz(th1.right,th2)
            return res
        return kruz(root,None)
            