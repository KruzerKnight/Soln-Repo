# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def inorder(th):
            if th==None:
                return
            
            inorder(th.left)
            l.append(th.val)
            inorder(th.right)
        inorder(root)
        return l