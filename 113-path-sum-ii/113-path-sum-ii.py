# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        l=[]
        def kruz(th,s,r):
            if th==None:
                return
            s+=th.val
            r+=' '+str(th.val)
            #print(r)
            if th.left==None and th.right==None:
                if targetSum==s:
                    l.append(r.split())
            kruz(th.left,s,r)
            kruz(th.right,s,r)
        kruz(root,0,'')
        return l