# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d=defaultdict(int)
        def inorder(th):
            if th==None:
                return
            inorder(th.left)
            d[th.val]+=1
            inorder(th.right)
        inorder(root)
        k=max(d.values())
        l=[]
        for i in d:
            if d[i]==k:
                l.append(i)
        return l