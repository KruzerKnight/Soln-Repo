# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root1 and root2:
            ans=TreeNode(root1.val+root2.val)
            ans.left=self.mergeTrees(root1.left,root2.left)
            ans.right=self.mergeTrees(root1.right,root2.right)
        elif root1 is None:
            ans=root2
        elif root2 is None:
            ans=root1
        else:
            ans=None
        return ans