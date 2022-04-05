# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=deque()
        q.append(root)
        r=[]
        if root==None:
            return []
        while q:
            cur=[]
            for _ in range(len(q)): #for same level of 
                i=q.popleft()
                cur.append(i.val)
                if i.left!=None:
                    q.append(i.left)
                if i.right!=None:
                    q.append(i.right)
            r.append(cur)
        return r