# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node=root
        while node:
            if node.val==val:
                return node
            elif node.val<val:
                node=node.right
            else:
                node=node.left
        return None
    
    #use the properties of a binary search tree, if val to found is less than the current nodes value go to left otherwise go to right