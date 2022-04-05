"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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
                for child in i.children:
                    q.append(child)
            r.append(cur)
        return r